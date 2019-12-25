from flask import Flask, request, jsonify,render_template, redirect, url_for,abort
import os
import logging
from werkzeug.utils import secure_filename
app = Flask(__name__)
visited=False

ALLOWED_EXTENSIONS = {'csv','xlsx'}
uploads_dir = os.path.join(os.getcwd(), 'uploads')
upload_chunk=os.path.join(os.getcwd(),'chunksuploader')
ct=0
#checking for the allowed file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    
    return render_template("index.html")

@app.route("/resumable_upload", methods=['GET'])
def resumable():
    resumableIdentfier = request.args.get('resumableIdentifier', type=str)
    resumableFilename = request.args.get('resumableFilename', type=str)
    resumableChunkNumber = request.args.get('resumableChunkNumber', type=int)

    if not resumableIdentfier or not resumableFilename or not resumableChunkNumber:
        
        abort(500, 'Parameter error')

    # chunk folder path based on the parameters
    temp_dir = os.path.join(upload_chunk, resumableIdentfier)

    # chunk path based on the parameters
    chunk_file = os.path.join(temp_dir, get_chunk_name(resumableFilename, resumableChunkNumber))
    #app.logger.debug('Getting chunk: %s', chunk_file)

    if os.path.isfile(chunk_file):
        # Let resumable.js know this chunk already exists
        return 'OK'
    else:
        # Let resumable.js know this chunk does not exists and needs to be uploaded
        abort(404, 'Not found')






@app.route('/upload',methods=['POST'])
def fileUploadHandler():
    global ct
    global visited
    ct+=1
    resumableTotalChunks = request.form.get('resumableTotalChunks', type=int)
    resumableIdentfier = request.args.get('resumableIdentifier', type=str)
    resumableFilename = request.args.get('resumableFilename', type=str)
    resumableChunkNumber = request.args.get('resumableChunkNumber', type=int)
    #storing the file
    uploadedFile=request.files['file']
    #print(resumableChunkNumber,resumableFilename,resumableIdentfier,end="\n\n\n")
    chunk_name = get_chunk_name(resumableFilename, resumableChunkNumber)
    #Chunks are uploaded 
    uploadedFile.save(os.path.join(upload_chunk,chunk_name))
<<<<<<< HEAD
    #print("here",visited)
=======
    print("here",visited)
>>>>>>> 9ccf2c399475d92a1596a6d1cd3edc22e226fbee
    if ct==resumableTotalChunks and visited==False:
       
        chunk_paths = [os.path.join(upload_chunk, get_chunk_name(resumableFilename, x)) for x in range(1, resumableTotalChunks+1)]
        upload_complete = all([os.path.exists(os.path.join(upload_chunk,p)) for p in chunk_paths])
        visited_dict={}
        for p in chunk_paths:
            visited_dict[p]=False
        if upload_complete:
            #ct+=1
            
            target_file_name = os.path.join(uploads_dir, resumableFilename)
            with open(target_file_name, "ab") as target_file:
                for p in chunk_paths:
                    stored_chunk_file_name = p
                    if visited_dict[stored_chunk_file_name]==False:
                        stored_chunk_file = open(stored_chunk_file_name, 'rb')
                        target_file.write(stored_chunk_file.read())
<<<<<<< HEAD

=======
                    #visited_dict[stored_chunk_file_name]=False
                    #print(visitetd_dict)
>>>>>>> 9ccf2c399475d92a1596a6d1cd3edc22e226fbee
                        stored_chunk_file.close()
                        
                    if visited_dict[stored_chunk_file_name]==False:
                        #ct+=1
                        #print(visited_dict[stored_chunk_file_name])
                        #stored_chunk_file.close()
                        visited_dict[stored_chunk_file_name]=True
<<<<<<< HEAD
                    #    try:
                        os.unlink(stored_chunk_file_name)
            #            except PermissionError: 
             #               print("Permission denied")
=======
                        try:
                             os.unlink(stored_chunk_file_name)
                        except PermissionError: 
                            print("Permission denied")
>>>>>>> 9ccf2c399475d92a1596a6d1cd3edc22e226fbee
                        
                
        
                target_file.close()
        visited=True
        print("Counter ",ct)
        

       
    return 'OK'


def get_chunk_name(uploaded_filename, chunk_number):
    return uploaded_filename + "_part_%03d" % chunk_number


if __name__ == "__main__":
<<<<<<< HEAD
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
    if not os.path.exists(upload_chunk):
        os.makedirs(upload_chunk)
    
    app.run(debug=True,host='0.0.0.0')
=======
    
    app.run(debug=True)
>>>>>>> 9ccf2c399475d92a1596a6d1cd3edc22e226fbee
