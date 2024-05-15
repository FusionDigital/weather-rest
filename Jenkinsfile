pipeline {
    agent {
      kubernetes {
          inheritFrom 'dind-agent'
      }
  }
  environment {
      DOCKER_CREDS = credentials('Docker_creds')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t revdennis/weather-rest .' 
      }
    }
    stage('Push') {
      steps {
        sh 'docker login -u $DOCKER_CREDS_USR -p $DOCKER_CREDS_PSW'
        sh 'docker push revdennis/weather-rest:latest'
      }
    }
    stage('Deploy') {
      steps {
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f service.yaml'
      }
    }
  }
}

