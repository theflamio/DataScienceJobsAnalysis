pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Unittest') {
            steps {
                 withPythonEnv('python3') {
                    sh 'pip install pytest'
                    sh 'pytest DB_handler_test.py'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
