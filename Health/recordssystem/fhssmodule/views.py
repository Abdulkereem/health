from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for,abort
from werkzeug.security import generate_password_hash, check_password_hash
import random
from models.Hcp import *
from models.enrollee import * 
import shortuuid
import nexmo


fhss = Blueprint('fhss', __name__)

def fhss_required():
    if current_user.fhss_role==False:
        return abort(404)
    else:
        pass

@fhss.route('/fhss')
@login_required
def fmain():
    fhss_required()
    #user = Enrollee.query.order_by(
    #Enrollee.date_registerd.desc()).all()
    user = Enrollee.query.filter_by(enrollee_role=True).all()
    hmos = Enrollee.query.filter_by(hmo_role=True).all()

    return render_template('./fhss/dashboard.html',user=user,hmos=hmos)
    
@fhss.route('/fenrollee')
@login_required
def fhenrol():
    fhss_required()
    user = Enrollee.query.filter_by(enrollee_role=True).all()
    return render_template('/fhss/enrollee/dashboard.html',user=user)
@fhss.route('/fhcp')
def fhcp():
    hcp = Enrollee.query.filter_by(hcp_role=True).all()
    return render_template('./fhss/hcp/hcp.html',hcp=hcp)

@fhss.route('/view_request/<int:id>')
def view_request(id):
    user = payments_claims.query.filter_by(Hmo_ID=id).all()
    return render_template('fhss/payments.html',user=user)


@fhss.route('/view_enrollee/<int:id>')
def view_enrollee(id):
    user = Enrollee.query.filter_by(id=id).first()
    return render_template('/fhss/enrollee/profile.html', user=user)


@fhss.route('/hcp_view/<int:id>')
def hcp_view(id):
    user = Enrollee.query.filter_by(id=id).first()
    return render_template('/fhss/hcp/profile.html', user=user)


@fhss.route('/view_history/<int:id>')
@login_required
def view_history(id):
    fhss_required()
    user = Histories.query.filter_by(Hospital_ID=id).all()
    return render_template('./fhss/hcp/view.html', user=user)





@fhss.route('/fprofile/<int:id>')
@login_required
def fprofile(id):
    fhss_required()
    user = Enrollee.query.filter_by(id=id).first()
    return render_template('/fhss/profile.html', user=user)

@fhss.route('/fhss/signup')
def fsignup():
    return render_template('fhss/signup/index.html')



