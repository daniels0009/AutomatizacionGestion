pipeline {
agent any stages {
stage('Build') {
steps {
sh 'echo "Hola Mundo"'
sh ''' echo "Múltiples líneas permiten escalonar el trabajo"
ls –lah
'''
}
}
}
}
