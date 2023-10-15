from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User 
from flask_app.models.message import Message 
from flask_bcrypt import Bcrypt


@app.route('/send_message', methods=['POST'])
def send_message():
        print(request.form)
        if not Message.validate_entry(request.form):
            return redirect('/dashboard')
        data = {
        "receiver_id" : request.form.get("receiver_id"),
        "sender_id" : request.form.get("sender_id"),
        "message" : request.form.get("message")}
        Message.save(data)
        return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete_message(id):
    data = {'id': id}
    Message.delete_message(data)
    return redirect ('/dashboard')