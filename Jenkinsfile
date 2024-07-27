pipeline {
    agent any

    stages {
        // stage('Checkout') {
        //     steps {
        //         // Checkout the code from the repository
        //         git 'https://github.com/your-repo/TodoApp.git' // Replace with your repo URL
        //     }
        // }

        stage('Build') {
            steps {
                // Restore dependencies and build the project
                script {
                    sh 'dotnet restore'
                    sh 'dotnet build --configuration Release'
                }
            }
        }

        stage('Test') {
            steps {
                // Run unit tests
                script {
                    sh 'dotnet test'
                }
            }
        }

        stage('Publish') {
            steps {
                // Publish the application
                script {
                    sh 'dotnet publish -c Release -o ./publish'
                }
            }
        }

        // stage('Deploy') {
        //     steps {
        //         // Deploy the application (adjust to your deployment method)
        //         script {
        //             // Here, you could use SSH, FTP, or any other method to deploy
        //             // Example: Uploading files to a server
        //             // sh 'scp -r ./publish/* user@server:/path/to/deploy'
        //         }
        //     }
        // }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
