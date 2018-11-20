pipeline {
    agent any
    stages {
        stage('Build') {
           withMaven(maven: 'M3',){
               sh 'mvn -B -DskipTests clean package'
           }
            //steps {
              //  sh 'mvn -B -DskipTests clean package'
            //}
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
