pipeline {
    agent {
        docker {
            image 'node:6-alpine'
            args '-p 3000:3000'
        }
    }
    environment {
        CI = 'true'
    }
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
                
                // yarn start
            }
        }
        stage('Test') {
            steps {
                chmod '+x ./jenkins/scripts/test.sh'
                sh './jenkins/scripts/test.sh'
            }
        }
    }
}
