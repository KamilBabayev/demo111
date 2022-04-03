pipeline {
         agent any
         stages {
                 stage('Build') {
                 steps {
                     echo 'Hi, GeekFlare. Starting to build the App.'
                     echo "${GIT_BRANCH}"
                     echo "${GIT_URL}"
                     script {
                              gv = load "custom.groovy"
                              gv.buildApp()
                     }
                     
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
                    script {
                           gv.testApp()      
                    }
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
                              script {
                                    gv.deployApp()
                              }
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
