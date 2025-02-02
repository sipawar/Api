pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
        // Ensure the directory containing python.exe is in PATH
        PATH = "C:\\Users\\siddhikaarjun_pawar\\AppData\\Local\\Programs\\Python\\Python313;$PATH"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm  // Assuming SCM setup is configured in Jenkins project settings
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Creating a virtual environment in the .venv directory
                    bat 'python -m venv .venv'

                    // Activating the virtual environment
                    bat 'call .venv\\Scripts\\activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Ensure virtual environment is activated before installing dependencies
                    bat 'call .venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Running pytest and generating a JUnit-compatible XML report
                    bat 'call .venv\\Scripts\\activate && pytest --junitxml=results.xml'
                }
            }
            post {
                always {
                    // Publish the JUnit test results
                    junit 'results.xml'
                }
            }
        }
    }
    post {
        always {
            // Deactivate and clean up if needed
            script {
                bat 'call .venv\\Scripts\\deactivate'
            }
        }
    }
}