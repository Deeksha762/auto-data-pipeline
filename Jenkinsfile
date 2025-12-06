pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Build Docker Image') {
      steps { sh 'docker build -t auto-data-pipeline:latest .' }
    }
    stage('Run Pipeline') {
      steps {
        sh 'mkdir -p output'
        sh 'docker run --rm -v $PWD/output:/app/output auto-data-pipeline:latest'
      }
    }
  }
  post {
    success { echo 'Chart generated: output/chart.png' }
  }
}
