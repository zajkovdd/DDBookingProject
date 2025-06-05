pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                // Шаг создания виртуального окружения и активации его
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                // Установка зависимостей из requirements.txt
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                // Запуск тестов и генерация отчёта Allure
                sh 'python3 -m pytest --alluredir allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    // Публикация Allure-отчётов (если установлен плагин Allure)
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            // Сохранение отчётов о тестировании и других артефактов
            archiveArtifacts artifacts: '**/allure-results/**', allowEmptyArchive: true
        }
        failure {
            // Если сборка провалилась, отправить уведомление или выполнить другое действие
            echo 'The build failed!'
        }
    }
}