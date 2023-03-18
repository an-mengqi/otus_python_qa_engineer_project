pipeline {
    agent any

    stages {
        stage('DockerBuild') {
            steps {
                echo 'CURRENT WORKSPACE: ${env.WORKSPACE}'
                echo 'Building docker image with tag tests'
                sh 'docker-compose build -t tests .'
            }
        }
    }
}
