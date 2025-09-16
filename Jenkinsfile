pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "sachinkiet"   // or private registry
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
				url: 'https://eos2git.cec.lab.emc.com/Sachin-Shukla/fastapi_micro_service_arch.git',
				credentialsId: '2b561b67-2fce-4300-96c8-9f69d27265f8'
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
                // ✅ Credentials block here
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_PASS')]) {
                    
                    sh """
                        echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin
                        docker push ${DOCKER_REGISTRY}/user_service:${DOCKER_TAG}
                        docker push ${DOCKER_REGISTRY}/task_service:${DOCKER_TAG}
                    """
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    sh "docker compose down || true"
                    sh "docker compose up -d"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
        success {
            echo 'Pipeline succeeded ✅'
        }
    }
}