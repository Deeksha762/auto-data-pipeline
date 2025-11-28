pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t auto-data-pipeline .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run --rm auto-data-pipeline'
            }
        }
    }
}
