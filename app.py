from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Configuración de la conexión a la base de datos Access
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ=C:\Users\alexa\Documents\Documentos U Jesús\BPDS 2023-2\RubricaBP\RubricaBP.accdb;')


@app.route('/')
def mostrar_reporte():
    # Consulta SQL para seleccionar los datos de la primera tabla
    cursor1 = conn.cursor()
    cursor1.execute('SELECT * FROM Cursos')
    data1 = cursor1.fetchall()

    # Consulta SQL para seleccionar los datos de la segunda tabla
    cursor2 = conn.cursor()
    cursor2.execute('SELECT * FROM Estudiantes')
    data2 = cursor2.fetchall()

    # Se cierran las conexiones
    cursor1.close()
    cursor2.close()
    conn.close()

    # Se hace un renderizado del template HTML con todos los datos de ambas tablas
    return render_template('ReporteBD.html', data1=data1, data2=data2)


if __name__ == '__main__':
    app.run(debug=True)
