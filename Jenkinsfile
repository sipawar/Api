pipeline {
    agent any

    environment {
        // Define environment variables if needed
        PYTHONPATH = '.'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python') {
            steps {
                script {
                    // Ensure Python and pytest are available, you can also set up a virtual environment
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Pytest') {
            steps {
                script {
                    // Running pytest
                    sh 'pytest --junitxml=reports/results.xml'
                }
                post {
                    always {
                        // Publish pytest reports using JUnit
                        junit 'reports/*.xml'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                // Add deployment steps if necessary
                sh './deploy_script.sh'
            }
            when {
                branch 'main' // Assuming deployment happens from the main branch
            }
        }
    }
}