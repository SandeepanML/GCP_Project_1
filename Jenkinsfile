pipeline{
    agent any

    environment{
        VENV_DIR = "venv"
    }

    stages{
        stage("Cloning the GITHUB repo to Jenkins"){
            steps{
                script{
                    echo "Cloning Started from GITHUB folder................."
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/SandeepanML/GCP_Project_1.git']])
                }
            }
        }

        stage("Setting up the Virtual Environments and Installing Dependencies"){
            steps{
                script{
                    echo "Setting up the Virtual Environments and Installing Dependencies................."
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}