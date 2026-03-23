pipeline {
    agent any

    environment {
        // Keeping your RDS details for the test stage
        DB_HOST = "database-2.cxkem6osoya0.us-east-2.rds.amazonaws.com"
        DB_NAME = "bankdb"
        DB_USER = "postgres"
        DB_PASSWORD = "Test123"
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

        // STEP 2: Verify the RDS connection (Still useful!)
        stage('Test RDS Connection') {
            steps {
                sh '''
                    PGPASSWORD=$DB_PASSWORD psql \
                    -h $DB_HOST \
                    -U $DB_USER \
                    -d $DB_NAME \
                    -c "SELECT 1;" 
                '''
            }
        }

        // STEP 3: Run the Application (This is the fix!)
        stage('Run Application') {
            steps {
                echo "Deploying the container..."
                // 1. Remove the old container if it exists so we don't get a name conflict
                // 2. Run the new one in the background (-d)
                sh """
                docker rm -f ${CONTAINER_NAME} || true
                docker run -d -p 8000:8000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
                """
                echo "Application is running in the background. Build complete!"
            }
        }
    }
}
