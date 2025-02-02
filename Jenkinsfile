pipeline {
    agent any

    parameters {
        // Define parameter used in 'Run Tests' stage
        string(name: 'task', defaultValue: 'default_task', description: 'Task to run')
    }

    environment {
        PYTHONPATH = '.'
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
                    // Creating and activating the virtual environment
                    bat 'python -m venv .venv'
                    bat 'call .venv\\Scripts\\activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    bat 'call .venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests on task: ${params.task}"
                    // Activate the virtual environment and run tests using pytest
                    bat """
                        call .venv\\Scripts\\activate
                        pytest --get_task=${params.task} --junitxml=test-results.xml
                    """
                }
            }
            post {
                always {
                    // Ensure to use the correct results file name
                    junit 'test-results.xml'
                }
            }
        }
    }
    post {
        always {
            // Deactivate the virtual environment and clean up
            script {
                bat 'call .venv\\Scripts\\deactivate'
            }
        }
    }
}