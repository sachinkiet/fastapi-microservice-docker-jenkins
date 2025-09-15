pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "sachinkiet"   // DockerHub username or registry name
        DOCKER_TAG = "latest"
    }

    tools {
        git 'Git-2.43.0'
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
                script {
                    withCredentials(
                    [
                        usernamePassword(
                            credentialsId: 'dockerhub-creds',
                            usernameVariable: 'DOCKER_USER',
                            passwordVariable: 'DOCKER_PASS'
                        )
                    ]) {
                        sh """
                            echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin
                            docker push ${DOCKER_REGISTRY}/user_service:${DOCKER_TAG}
                            docker push ${DOCKER_REGISTRY}/task_service:${DOCKER_TAG}
                        """
                    }
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                script {
                    // stop existing containers, ignore errors if not running
                    sh "docker compose down || true"
                    // start new containers in detached mode
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