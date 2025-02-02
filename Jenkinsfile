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
                    bat 'call .venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests on task: ${params.task}"
                    def attempts = 3
                    def runTests = {
                        bat """
                            call .venv\\Scripts\\activate
                            pytest -v -s --get_task=${params.task} --junit-xml=test-results.xml
                        """
                        // If the bat command fails, it throws an exception and retry logic kicks in
                    }
                    retry(attempts) {
                        runTests()
                    }
                }
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
    post {
        always {
            script {
                bat 'call .venv\\Scripts\\deactivate'
            }
            deleteDir() // Clean workspace after the run for a fresh start next time
        }
    }
}