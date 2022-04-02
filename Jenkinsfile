pipeline {
         agent any
         stages {
                 stage('Build') {
                 steps {
                     echo 'Hi, GeekFlare. Starting to build the App.'
                 }
                 }
                 stage('install prerequsitives') {
                 steps {
                    sh  'pip3 install requests'
                 }
                 }
                 stage('Test') {
                 steps {
                    sh 'python3 demo.py'
                 }
                 }
                 stage('Deploy') {
                 parallel { 
                            stage('Deploy start ') {
                           steps {
                                echo "Start the deploy .."
                           } 
                           }
                            stage('Deploying now') {
                            agent any
                              steps {
                                echo "Docker Created"
                              }
                           }
                           }
                           }
                 stage('Prod') {
                     steps {
                                echo "App is Prod Ready"
                              }
                 
                 }
                 stage('Flake8 install and test') {
                     steps {
                         script {
                             'pip3 install flake8',
                             'flake8 .'
                         }         
                     }
                 }
}
}
