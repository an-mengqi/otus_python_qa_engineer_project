pipeline {
    agent any

    stages {
        stage('DockerBuild') {
            steps {
                sh 'mkdir logs'
                sh 'ls'
                echo 'CURRENT WORKSPACE: ${env.WORKSPACE}'
                echo 'Building docker image with tag tests'
                sh 'docker-compose build'
                sh 'docker-compose up'
            }
        }
    }
     post {

        always {sh 'docker-compose down'}
     }
}
