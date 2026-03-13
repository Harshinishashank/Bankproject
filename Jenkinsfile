pipeline {
    agent any

    environment {
        DB_HOST = "database-2.cxkem6osoya0.us-east-2.rds.amazonaws.com"
        DB_NAME = "bankdb"
        DB_USER = "postgres"
        DB_PASSWORD = "Test1234"
    } // <-- This bracket closes the environment block

    stages { // <-- This starts the container for ALL stages
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test RDS Connection') {
            steps {
                sh '''
                    PGPASSWORD=$DB_PASSWORD psql \
                    -h $DB_HOST \
                    -U $DB_USER \
                    -d $DB_NAME \
                    -c "SELECT * FROM users;"
                '''
            }
        }

        stage('Run Application') {
            steps {
                // Using ./venv/ (local) instead of ~/venv/ (home) to match your install stage
                sh './venv/bin/python manage.py runserver 0.0.0.0:8000'
            }
        }
    } // <-- This closes the stages block
} // <-- This closes the pipeline
