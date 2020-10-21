pipeline {
  agent any
  stages {
    stage('test') {
      steps {
        ws(dir: '/tmp/test') {
          sh '''python3 -m venv test_jenkins
source test_jenkins/bin/activate
pip install -r requirements.txt
pytest test.py'''
        }

      }
    }

    stage('depkoy') {
      steps {
        echo 'this is deploy'
      }
    }

  }
}