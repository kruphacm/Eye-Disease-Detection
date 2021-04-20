import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('HTMLeye.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x)-1 for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = abs(int(prediction[0]))
    res={0:'Cataract Treatment:Surgery',1:'Glaucoma    Treatment:Medical and Surgery',2:'Eye strain   Treatment:Artificial tears',3:'Refractive Errors    Treatment:Eyeglasses,Contact lenses,Refractive surgery',4:'Dry eye Syndrome    Treatment:Artificial tears',5:'Diabetic Retinopathy    Treatment:Management of Diabetes,laser treatment,Surgery',6:'Conjunctivitis    Treatment:Antibiotic/ antihistaminic eye drops or ointments'}
    output=res[output]

    return render_template('HTMLeye.html', prediction_text='Predicted Disease is {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)