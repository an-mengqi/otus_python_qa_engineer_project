pipeline {
    agent any

    stages {
        stage('DockerBuild') {
            steps {
                sh 'mkdir -p logs'
                sh 'ls'
                echo 'Building docker image with tag tests'
                sh 'docker-compose build'
                sh 'docker-compose up'
                sh 'echo DOCKER COMPOSE WAS UP'

            }
        }
    }
       post {

        always {sh 'echo SOMETHING'}
        }
}
