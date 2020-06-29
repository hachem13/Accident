#!/usr/bin/env python
# coding: utf-8


# import librery 
from app import app
from app.models import *
from flask import render_template, request
from app.config import create_plot, create_plot1, create_plot2
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required

# secret key
app.config['SECRET_KEY'] = 'A2444EES'

class loginForm(FlaskForm):
  """ call year from index.html"""
  year = StringField('year', validators=[input_required()])
  age1 = StringField('age1')
  age2 = StringField('age2')
# Création de route index (page principale)
@app.route('/', methods = ['GET', 'POST'])
def index():
  """ call index.html in template """
# treatment of dataframe and query
  names=['code_departement', 'nom_departement', 'code_region', 'nom_region']
  df = pd.read_csv('/Users/mosbahhachem/Documents/git/Accident/departements-france.csv',
                            header=None, skiprows=[0], names=names)
  list_code_departement = df.code_departement.tolist()
  list_nom_departement = df.nom_departement.tolist()

  list_code_departement1 = []
  list_code_departement2 = [971,972,973,974,976]

  for i in range(1, len(list_code_departement)-5):
      i = i*10
      list_code_departement1.append(i)
      
  list_code_departement = list_code_departement1 + list_code_departement2
  list_code_departement.insert(29, 201)
  list_code_departement.insert(30, 202)
  list_code_departement.remove(200)

  form = loginForm()
# condition validation constraint 
  if form.validate_on_submit():
    return 
  else:
    return render_template('index.html', list_code_departement=list_code_departement, list_nom_departement=list_nom_departement, form=form)
  

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
  """ call dashbord.html in tamplate """
# request method for post
  request.method == 'POST'

# call variable to tamplate index.html
  year = request.form.get('year')
  departement = request.form.get('departement')


  unhurt = request.form.get('unhurt') != None
  dead = request.form.get('dead') != None
  
  hospitalize = request.form.get('hospitalize') != None
  hurt_light =request.form.get('hurt_light') != None

  age1 = request.form.get('age1')
  age2 = request.form.get('age2')

  men = request.form.get('men')!= None
  women = request.form.get('women')!= None

# call fonction creat_plot from file config.py  
  plot1 = create_plot(year, departement ,1, 1, age1, age2, "USAGERS ACCIDENTÉS : HOMMES-INDEMNES", 'rgba(230, 36, 36, 0.5)')
  plot2 = create_plot(year, departement,1, 2, age1, age2, "USAGERS ACCIDENTÉS : HOMMES-TUER", 'rgba(4, 0, 247, 0.5)')
  plot3 = create_plot(year, departement, 1,  3, age1, age2, "USAGERS ACCIDENTÉS : HOMMES-BLESSÉES HOSPITALISÉES" , 'rgba(54, 214, 71, 0.5)')
  plot4 = create_plot(year, departement,1, 4 , age1, age2, "USAGERS ACCIDENTÉS : HOMMES-BLESSÉES LEGERÉES",'rgba(0, 0, 0, 0.5)')
  plot5 = create_plot(year, departement ,2, 1, age1, age2, "USAGERS ACCIDENTÉS : FEMMES-INDEMNES", 'rgba(230, 36, 36, 0.5)')
  plot6 = create_plot(year, departement,2, 2, age1, age2, "USAGERS ACCIDENTÉS : FEMMES-TUER" ,'rgba(4, 0, 247, 0.5)')
  plot7 = create_plot(year, departement, 2,  3, age1, age2, "USAGERS ACCIDENTÉS : FEMMES-BLESSÉES HOSPITALISÉES", 'rgba(54, 214, 71, 0.5)')
  plot8 = create_plot(year, departement,2, 4 , age1, age2, "USAGERS ACCIDENTÉS : FEMMES-BLESSÉES LEGERÉES", 'rgba(0, 0, 0, 0.5)')
  plot9 = create_plot1(year)
  plot10 = create_plot2(year)
# return the tamplate
  return render_template('graph.html', plot1= plot1, plot2 = plot2, plot3 = plot3, plot4 = plot4, plot5 = plot5, plot6 = plot6, plot7 = plot7, plot8 = plot8,plot9=plot9,plot10 = plot10, unhurt = unhurt, dead = dead, 
    hospitalize= hospitalize,hurt_light= hurt_light, age1= age1, age2= age2, men = men, women= women, year=year)
  
 