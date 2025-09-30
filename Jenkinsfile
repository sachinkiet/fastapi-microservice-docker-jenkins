pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root:root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        DOCKER_REGISTRY = "sachinkiet"
        DOCKER_TAG = "latest"
    }

    stages {
		stage('Setup Tools') {
            steps {
                sh '''
                    apt-get update && apt-get install -y make git
                '''
            }
        }
	
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
                    pip install --upgrade pip
                    pip install pylint black pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh 'make lint'
            }
        }

        stage('Format Check') {
            steps {
                sh 'make format'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'make test'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'make docker-build'
            }
        }

        stage('Push Docker Images') {
            steps {
                sh 'make docker-push'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'make docker-deploy'
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "Pipeline succeeded ✅"
        }
        failure {
            echo "Pipeline failed ❌"
        }
    }
}