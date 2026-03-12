pipeline {
    agent any

    environment {
        DB_HOST = "database-2.cxkem6osoya0.us-east-2.rds.amazonaws.com"
        DB_NAME = "bankdb"
        DB_USER = "postgres"
        DB_PASSWORD = "Test1234"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                ~/venv/bin/pip install -r requirements.txt
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
                sh '''
                ~/venv/bin/python manage.py runserver 0.0.0.0:8000
                '''
            }
        }

    }
}
