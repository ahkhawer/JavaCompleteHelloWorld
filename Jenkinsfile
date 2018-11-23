pipeline {
  agent any

  stages {
      stage('Build') {
        steps {

          echo 'Changing directory to features'
          sh 'cd features'
          echo 'Running lettuce command'
          sh 'lettuce'
        }
      }
      stage('Test') {
        steps {

        }
        post {
          always {

          }
        }
      }
      stage('Deliver') {
        steps {
          
        }
      }
  }
}
