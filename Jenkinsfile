pipeline {
         agent any
         stages {
                 stage('Build') {
                 steps {
                     echo 'Hi, GeekFlare. Starting to build the App.'
                     echo "${env.BRANCH_NAME}"
                     echo "${GIT_BRANCH}"
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
                                           stage('Prod') {
                     steps {
                                echo "App is Prod Ready"
                              }
                 
                 }
                 stage('Flake8 install and test') {
                     steps {
                         sh """
                         pip3 install pytest
                         pytest .
                         flake8 .
                         """
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

}
}
