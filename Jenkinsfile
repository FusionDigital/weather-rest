pipeline {
  agent none
  stages {
    stage('build and Push') {
    agent { kubernetes { inheritFrom 'dind-agent' } }
    environment { DOCKER_CREDS = credentials('Docker_creds') }
      steps {
        sh 'docker build -t revdennis/weather-rest .' 
        sh 'docker login -u $DOCKER_CREDS_USR -p $DOCKER_CREDS_PSW'
        sh 'docker push revdennis/weather-rest:latest'
      }
    }
    stage('Deploy') {
    agent { kubernetes { inheritFrom 'kubectl' } }
      steps {
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f service.yaml'
      }
    }
  }
}

