pipeline {
    agent { label "aws"}
    stages {
        stage('Build Docker Container') {
            steps {
                sh 'docker build -t gpw .'
            }
        }
        stage('Run Docker Container'){
            steps{
                sh 'docker run --rm gpw'
            }        
        }
    }
}
