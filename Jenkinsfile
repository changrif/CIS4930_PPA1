pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python3 -m py_compile main/bmi.py main/email.py main/shortestDistance.py main/tab.py main/main.py'
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'pytest --verbose --junit-xml test-reports/results.xml --cov=main tests/' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}