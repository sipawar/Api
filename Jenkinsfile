pipeline {
    agent any

    stages {
        stage('Setup Environment Variables') {
            steps {
                script {
                    // Dynamically set the PATH to include the Python directory according to the agent's OS
                    if (isUnix()) {
                        sh 'export PATH=$PATH:$PYTHON_DIR'
                    } else {
                        bat 'set PATH=%PATH%;%PYTHON_DIR%'
                    }
                }
            }
        }

        stage('Checkout Code') { // Added missing opening brace here
            steps {
                checkout scm // Assuming SCM setup is configured in Jenkins project settings
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Use environmental variable for python execution
                    bat '%PYTHON_DIR%\\python -m venv .venv'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'call .venv\\Scripts\\activate && pip install -r requirements.txt'
                    // Ensure pytest-rerunfailures is installed along with other dependencies
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests on task: ${params.task}"
                    bat """
                        call .venv\\Scripts\\activate
                        pytest -v -s --get_task=${params.task} --junit-xml=test-results.xml --reruns 3
                    """
                    // Integration of pytest-rerunfailures with reruns flag
                }
            }
            post {
                always {
                    junit 'test-results.xml'
                    // Collect and record test reports
                }
            }
        }
    }
    post {
        always {
            script {
                bat 'call .venv\\Scripts\\deactivate'
                // Deactivate the Python virtual environment
            }
            deleteDir() // Clean workspace after the run for a fresh start next time
        }
    }
}