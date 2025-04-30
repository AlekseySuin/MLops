pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/AlekseySuin/MLops.git'
            }
        }
        stage('Run Pipeline') {
            steps {
                sh 'chmod +x pipeline.sh'  // Даём права на выполнение
                sh './pipeline.sh'         // Запускаем основной скрипт
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/model.pkl', allowEmptyArchive: true
            junit '**/test_results.xml'    // Если есть тесты
        }
        failure {
            emailext body: 'Сборка провалилась: ${BUILD_URL}', subject: 'FAILED: ${JOB_NAME}', to: 'ваш@email.com'
        }
    }
}
