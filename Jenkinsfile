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
                sh 'echo DOCKER COMPOSE WAS UP'

            }
        }
    }
       post {

            always {
                echo 'Copying allure report from container'
                sh 'docker cp opencart_tests:/app/allure-results .'

                script {
                    allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'allure-results']]
                    ])
                }
            }
        }
}
