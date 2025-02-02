pipeline {
    agent any

    parameters {
        // Define parameter used in 'Run Tests' stage
        string(name: 'task', defaultValue: 'default_task', description: 'Task to run')
    }

    environment {
        PYTHONPATH = '.'
        // Ensure that PATH modification persists across all shell executions
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
                    // Creating and activating the virtual environment
                    bat 'python -m venv .venv'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Activate virtual environment and install dependencies
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
                        pytest --get_task=${params.task} --junit-xml=test-results.xml
                    """
                    // Note: Corrected '--junitxml' flag to '--junit-xml' for pytest
                }
            }
            post {
                always {
                    // Capture test results and utilize flaky test handling
                    junit 'test-results.xml'
                    step([$class: 'FlakyTestReporter',
                        testResultFile: 'test-results.xml', // Ensure file name matches generated XML
                        reRunTestResultFile: 'retest-results.xml',
                        maxRuns: 3,
                        reRunIfUnstable: true])
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
            // Clean-up step: Deleting virtual environment directory if needed
            deleteDir()
        }
    }
}