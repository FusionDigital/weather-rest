pipeline {
  agent dind
  stages {
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

