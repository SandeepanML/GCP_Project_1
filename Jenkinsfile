pipeline{
    agent any

    stages{
        stage("Cloning the GITHUB repo to Jenkins"){
            steps{
                script{
                    echo "Cloning Started from GITHUB folder................."
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/SandeepanML/GCP_Project_1.git']])
                }
            }
        }
    }
}