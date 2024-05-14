pipeline {
  agent any
  stages {
    tools {
        docker 'latest'
        jdk 'jdk17'
    }
    stage('Build') {
      steps {
        sh 'docker build -t weather-rest .' 
      }
    }
    stage('Push') {
      steps {
        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
        sh 'docker push weather-rest'
      }
    }
    stage('Deploy') {
      steps {
        sh 'kubectl apply -f weather-rest-deployment.yaml'
      }
    }
  }
}

