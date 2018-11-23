pipeline {
  agent any
  tools {
    maven 'M2_Home'
  }
  stages {
      stage('Build') {
        steps {
          sh 'mvn -B -DskipTests clean package'
        }
      }
      stage('Test') {
        steps {
          //sh 'mvn test'
          echo 'Changing directory to features'
          sh 'cd features'
          echo 'Running lettuce command'
          sh 'lettuce'
        }
        post {
          always {
            junit 'target/surefire-reports/*.xml'
          }
        }
      }
      stage('Deliver') {
        steps {
          sh './jenkins/scripts/deliver.sh'
        }
      }
  }
}
