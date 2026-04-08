pipeline {
    agent any

    environment {
        // Keeping your RDS details for the test stage
        DB_HOST = "database-2.cxkem6osoya0.us-east-2.rds.amazonaws.com"
        DB_NAME = "bankdb"
        DB_USER = "postgres"
        IMAGE_NAME = "bankproject:latest"
        CONTAINER_NAME = "bank-app"
    }

    stages {
        // STEP 1: Build the image using your Dockerfile
        stage('Build Docker Image') {
            steps {
                echo "Building the Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        // STEP 2: Verify the RDS connection (Secure Version)
        stage('Test RDS Connection') {
            steps {
                withCredentials([string(credentialsId: 'RDS_DB_PASSWORD', variable: 'DB_PASSWORD')]) {
                    sh '''
                        PGPASSWORD=$DB_PASSWORD psql \
                        -h $DB_HOST \
                        -U $DB_USER \
                        -d $DB_NAME \
                        -c "SELECT 1;" 
                    '''
                }
            }
        }

    stage('Run Application') {
            steps {
                echo "Deploying the container..."
                sh """
                docker rm -f ${CONTAINER_NAME} || true
                docker run -d -p 8000:8000 --memory='512m' --cpus='0.5' --restart always --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
                echo "Application is running with auto-restart enabled. Build complete!"
            } // Closes steps
        } // Closes stage
    } // Closes stages
} // Closes pipeline
