pipeline {
  agent any
  stages {
     stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
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
