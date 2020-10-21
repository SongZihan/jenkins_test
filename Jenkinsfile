pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        sh 'pytest test.py'
      }
    }

    stage('depkoy') {
      steps {
        echo 'this is deploy'
      }
    }

  }
}