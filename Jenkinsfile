pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "sachinkiet"     // Your DockerHub username or registry
        DOCKER_TAG = "${env.BUILD_NUMBER}" // Auto-tag images with Jenkins build number
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull source code from Git
                git branch: 'main',
                    url: 'https://eos2git.cec.lab.emc.com/Sachin-Shukla/fastapi_micro_service_arch.git',
                    credentialsId: '2b561b67-2fce-4300-96c8-9f69d27265f8'
            }
        }
		
		stage('Run Tests') {
			steps {
				// Run tests for user_service
				sh 'echo "Running tests for user_service..."'
				sh 'pip install -r user_service/requirements.txt'
				sh 'pytest user_service/tests -v'
				// Run tests for task_service
				sh 'echo "Running tests for task_service..."'
				sh 'pip install -r task_service/requirements.txt'
				sh 'pytest task_service/tests -v'
			}
		}

        stage('Build Docker Images') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REGISTRY}/user_service:${DOCKER_TAG} ./user_service"
                    sh "docker build -t ${DOCKER_REGISTRY}/task_service:${DOCKER_TAG} ./task_service"
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                // Use credentials securely without Groovy interpolation
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
                    sh "docker push ${DOCKER_REGISTRY}/user_service:${DOCKER_TAG}"
                    sh "docker push ${DOCKER_REGISTRY}/task_service:${DOCKER_TAG}"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    // Pull new images with version tag into docker-compose
                    sh "docker compose down || true"
                    // Optional: force re-pull of tagged images
                    sh "docker compose up -d --pull always"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        failure {
            echo "Pipeline failed ❌"
        }
        success {
            echo "Pipeline succeeded ✅"
        }
    }
}