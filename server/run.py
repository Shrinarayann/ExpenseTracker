from app import create_app
PORT=8080

app=create_app()

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=PORT)
     