pipeline {
    agent any

    parameters {
        string(name: 'task', defaultValue: 'default_task', description: 'Task to run')
    }

    environment {
        PYTHONPATH = '.'
        PATH = "${env.PATH};C:\\Users\\siddhikaarjun_pawar\\AppData\\Local\\Programs\\Python\\Python313"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm // Assuming SCM setup is configured in Jenkins project settings
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    bat 'python -m venv .venv'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'call .venv\\Scripts\\activate && pip install -r requirements.txt pytest-rerunfailures'
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
                        pytest -v -s  --get_task=${params.task} --junit-xml=test-results.xml --reruns 3
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