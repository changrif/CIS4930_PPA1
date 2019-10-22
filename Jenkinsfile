pipeline {
    agent {
        docker {
            image 'python:3-alpine'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python3 -m py_compile main/bmi.py main/email.py main/shortestDistance.py main/tab.py main/main.py api/api.py main/db.py console/console.py'
            }
        }
        stage('Unit Tests') { 
            steps {
                sh 'pytest --verbose --junit-xml test_reports/unit_tests.xml --cov=main unit_tests/' 
            }
            post {
                always {
                    junit 'test_reports/unit_tests.xml' 
                }
            }
        }
        
    }
}