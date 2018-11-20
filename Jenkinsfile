pipeline {
    agent any
    stages {
        stage('Build') {
        steps {
          script {
            withMaven(globalMavenSettingsConfig: "$mavenConfig", jdk: "$JDKVersion", maven: "$mavenLocation") {
            sh 'mvn -B -DskipTests clean package'
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
