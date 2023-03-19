pipeline {
    agent any

    stages {
        stage('DockerBuild') {
            steps {
                sh 'mkdir -p logs'
                echo 'Building docker image with tests'
                sh 'docker-compose build'
                sh 'docker-compose up --abort-on-container-exit'
            }
        }
    }
       post {

            always {
                echo 'Copying allure-results from container'
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
