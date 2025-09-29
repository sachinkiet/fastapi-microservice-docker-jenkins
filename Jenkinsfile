pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "sachinkiet"     // Your DockerHub username or registry
        DOCKER_TAG = "${env.BUILD_NUMBER}" // Auto-tag images with Jenkins build number
    }

	options {
        disableConcurrentBuilds()          // Avoid parallel runs locking workspace
        skipDefaultCheckout()              // We'll do our own checkout
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

        stage('Lint with Pylint') {
            steps {
                sh '''
                docker run --rm -v $PWD:/app -w /app python:3.11 bash -c "
                  pip install --break-system-packages pylint &&
                  pylint user_service/user_app task_service/task_app --disable=C0114,C0115,C0116
                "
                '''
            }
        }

		stage('Run Tests') {
			agent any
			steps {
				// Run user_service tests inside Python docker
				sh '''
				docker run --rm -v $PWD:/app -w /app -e HOME=/tmp python:3.11 bash -c "
				  pip install --break-system-packages -r user_service/requirements.txt &&
				  pytest user_service/tests -v
				"
				'''
				// Run task_service tests inside Python docker
				sh '''
				docker run --rm -v $PWD:/app -w /app -e HOME=/tmp python:3.11 bash -c "
				  pip install --break-system-packages -r task_service/requirements.txt &&
				  pytest task_service/tests -v
				"
				'''
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
		aborted {
			echo "Build aborted — cleaning up leftover containers..."
			sh 'docker compose down || true'
		}
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