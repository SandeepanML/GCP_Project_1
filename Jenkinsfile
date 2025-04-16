pipeline{
    agent any

    environment{
        VENV_DIR = "venv"
        GCP_PROJECT = "delta-array-456316-j9"
        GCLOUD_PATH = "var/jenkins_home/google-cloud-sdk/bin"
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

        stage("Building and Pushing Docker Image to GCR.."){
            steps{
                withCredentials([file(credentialsId : 'gcp-key', variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker Image to GCR..............'
                        sh '''
                        export PATH=$PATH:$(GCLOUD_PATH)

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
                }
            }
        }
    }
}