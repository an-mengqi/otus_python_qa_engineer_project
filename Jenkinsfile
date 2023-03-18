pipeline {
    agent any

    stages {
        stage('DockerBuild') {
            steps {
                sh 'mkdir -p logs'
                sh 'ls'
                echo 'Building docker image with tag tests'
                sh 'docker-compose build'
                sh 'docker-compose up --abort-on-container-exit'
            }
        }
    }
}
