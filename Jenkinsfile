pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "sachinkiet"
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    options {
        disableConcurrentBuilds()
        skipDefaultCheckout()
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://eos2git.cec.lab.emc.com/Sachin-Shukla/fastapi_micro_service_arch.git',
                    credentialsId: '2b561b67-2fce-4300-96c8-9f69d27265f8'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                docker run --rm -v $PWD:/app -w /app python:3.11 bash -c "
                  pip install --upgrade pip &&
                  pip install pylint black pytest &&
                  make install
                "
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                docker run --rm -v $PWD:/app -w /app python:3.11 bash -c "
                  make lint
                "
                '''
            }
        }

        stage('Format Check') {
            steps {
                sh '''
                docker run --rm -v $PWD:/app -w /app python:3.11 bash -c "
                  make format
                "
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                docker run --rm -v $PWD:/app -w /app python:3.11 bash -c "
                  make test
                "
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh "make docker-build DOCKER_REGISTRY=${DOCKER_REGISTRY} DOCKER_TAG=${DOCKER_TAG}"
            }
        }

        stage('Push Docker Images') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    sh 'echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
                    sh "make docker-push DOCKER_REGISTRY=${DOCKER_REGISTRY} DOCKER_TAG=${DOCKER_TAG}"
                }
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh "make docker-deploy"
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