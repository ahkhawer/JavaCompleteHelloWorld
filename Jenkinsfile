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
          sh 'mvn test'
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
