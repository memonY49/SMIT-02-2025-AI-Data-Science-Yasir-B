from flask import Flask, render_template, request, Response, redirect, url_for, flash
import cv2
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for flash messages


camera = cv2.VideoCapture(0)



DATASET_DIR = os.path.join("dataset")
os.makedirs(DATASET_DIR, exist_ok=True)
face= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
progress = {"name":"","total": 0, "captured": 0}


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            facedetect = face.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=1,)

            for x,y,w,h in facedetect:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html',progress=progress)


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/capture', methods=['POST'])
def capture():
    name = request.form['person_name'].strip()
    num_images = int(request.form['num_images'])

    if not name:
        flash("Name cannot be empty!")
        return redirect(url_for('index'))

    
    save_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(save_dir, exist_ok=True)

    count = 0
    while count < num_images:
        ret, frame = camera.read()
        if not ret:
            flash("Camera error!")
            return redirect(url_for('index'))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        facedetect = face.detectMultiScale(gray, 
                                           scaleFactor=1.3, 
                                           minNeighbors=1,
                                           minSize=(100, 100))
        if len(facedetect) == 0:
            continue
        
        progress = {"name": name, "total": num_images, "current": 0}

        (x, y, w, h) = facedetect[0]
        face_img = frame[y:y+h, x:x+w]

        img_path = os.path.join(save_dir, f"{count+1}.jpg")
        cv2.imwrite(img_path, face_img)
        count += 1
        progress["current"] = count
        cv2.waitKey(200)  

    progress = {"name": "", "total": 0, "current": 0}
    flash(f"Captured {num_images} images for {name}!")
    return redirect(url_for('index'))


app.run(host='0.0.0.0', port=5000, debug=True)
