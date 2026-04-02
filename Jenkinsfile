pipeline {
    agent any

    stages {
        stage('Checkout') {
    steps {
        git branch: 'main', url: 'https://github.com/manns1987/TICTO.git'
        }
                        }
        }

        stage('Setup Python') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest
                '''
            }
        }
    }
}