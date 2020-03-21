from flask import Flask
import query


app = Flask(__name__)
Q = query.Query(0)

@app.route('/topstory')
def topstory():
    return(Q.QueryTopStoryHeadline())

@app.route('/search/<query>/<count>')
def search(query,count=3):
    return(Q.Search(query,int(count)))

#IMPORTANT: ALWAYS CALL TOPSTORY BEFORE MAKING A CALL TO GETDOCUMENTTEXT()
@app.route('/topstory/more')
def more():
    return(Q.GetDocumentText())

#this is used for choosing a story, callback is from the returned json (the voice assistant will have to choose what story id the function gets called with)
@app.route('/topstory/more/<id>')
def searchid(id=0):
    return(Q.GetDocumentText(id))

if __name__ == '__main__' :
    app.run(host='10.0.0.101')































