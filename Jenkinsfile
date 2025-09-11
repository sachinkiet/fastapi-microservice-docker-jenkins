pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "your-dockerhub-username"   // or private registry
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-org/fastapi_micro_service_arch.git'
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
                script {
                    sh "echo \$DOCKERHUB_PASS | docker login -u \$DOCKERHUB_USER --password-stdin"
                    sh "docker push ${DOCKER_REGISTRY}/user_service:${DOCKER_TAG}"
                    sh "docker push ${DOCKER_REGISTRY}/task_service:${DOCKER_TAG}"
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
