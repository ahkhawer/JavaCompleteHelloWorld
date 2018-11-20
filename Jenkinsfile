pipeline {
    agent any
    stages {
        stage('Build') {
          steps {
            script {
              withMaven( maven: "/Applications/apache-maven-3.6.0") {
              sh 'mvn -B -DskipTests clean package'
              }
            }
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
