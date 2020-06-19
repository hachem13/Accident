#!/usr/bin/env python
# coding: utf-8

# import library

from sqlalchemy import create_engine
import pandas as pd
import plotly 
import plotly.graph_objs as go 
import json
from urllib.request import urlopen
import plotly.express as px 

# Relation between mysql and python
engine = create_engine("mysql+pymysql://hachem:tiger@localhost/ACCIDENT")

def create_plot(year, departement, gender, gravity, names, colors):
    """ treatment query and creat figure"""
 
    Query = pd.read_sql_query("SELECT annee,DEPARTEMENT, COUNT(GRAV)GRAVITÉ_USAGER                                                                                       , ( 2005 - annee_NAISSANCE) AGE                                                                   FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2005 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                 WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT,AGE                                                                         UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT , COUNT(GRAV)GRAVITÉ_USAGER                                                                                       , ( 2006 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                  JOIN CARACTERISTIQUE_2006 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                           UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV)GRAVITÉ_USAGER                                                                                       , ( 2007 - annee_NAISSANCE) AGE                                                                   FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2007 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                              WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                        UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                       , ( 2008 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                  JOIN CARACTERISTIQUE_2008 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                         UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                       , ( 2009 - annee_NAISSANCE) AGE                                                                   FROM USAGERS_%s U                                                                                  JOIN CARACTERISTIQUE_2009 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                              WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                        UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                       , ( 2010 - annee_NAISSANCE) AGE                                                                   FROM USAGERS_%s U                                                                                  JOIN CARACTERISTIQUE_2010 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                               WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                          UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                       , ( 2011 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2011 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                 WHERE U.GRAV =%s                                                                                  GROUP BY annee, DEPARTEMENT, AGE                                                                       UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                        , ( 2012 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2012 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                 WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                         UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                        , ( 2013 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2013 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                   WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                         UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT                                                                            , COUNT(GRAV) USAGER_MORT                                                                             , ABS( 2014 - annee_NAISSANCE) AGE                                                                   FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2014 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                         UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                       , ( 2015 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2015 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                               WHERE U.GRAV =%s                                                                                     GROUP BY annee, DEPARTEMENT, AGE                                                                          UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                        , ( 2016 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2016 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE =%s                                                                                                 WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                          UNION                                                                                                                                                                                                       SELECT annee, DEPARTEMENT, COUNT(GRAV) GRAVITÉ_USAGER                                                                                       , ( 2017 - annee_NAISSANCE) AGE                                                                    FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_2017 C ON U.NUM_ACC = C.NUM_ACC AND DEPARTEMENT ='%s'  AND SEXE = %s                                                                                               WHERE U.GRAV =%s                                                                                      GROUP BY annee, DEPARTEMENT, AGE                                                                                               ORDER BY AGE;"  %(year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement, gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity, year, departement , gender, gravity) ,  con = engine)


# Creat plot  
    fig = go.Bar(
                x = Query.AGE,
                y = Query.GRAVITÉ_USAGER,
                name = names,
                marker = dict(color = colors ,
                             line = dict(color ='rgb(0,0,0)',width =1.5)))
    data = [fig]
    layout = go.Layout(barmode = "group",
                       title= "ACCIDENT USAGERS EN FONCTION DE L'AGE",
                       xaxis=dict(title='Age'),
                       yaxis=dict( title="Nombre D'usager"))
    fig = go.Figure(data = data, layout = layout)

    """trace1 = go.Scatter(
                    x = Query.AGE,
                    y = Query.GRAVITÉ_USAGER,
                    mode = "lines",
                    name = names,
                    marker = dict(color = colors
                    ))
    data = [trace1]
    layout = dict(title = "",
              xaxis= dict(title='Age'),
              yaxis = dict(title="Nombre D'usager"))
    fig = go.Figure(data = data, layout= layout)"""


    graphJSON = json.dumps (fig, cls = plotly.utils.PlotlyJSONEncoder) 
    
    return graphJSON

def create_plot1(year):
    """ treatment of query and creat figure """
    QUERY1 = pd.read_sql_query("SELECT  DEPARTEMENT, COUNT(GRAV) Nombre_usagers_accidentés                                                                             FROM USAGERS_%s U                                                                                   JOIN CARACTERISTIQUE_%s C ON U.NUM_ACC = C.NUM_ACC                                                                                               GROUP BY DEPARTEMENT;" %(year, year), con = engine)
    
    with urlopen('https://france-geojson.gregoiredavid.fr/repo/departements.geojson') as response:
        geojson = json.load(response)
    names=['code_departement', 'nom_departement', 'code_region', 'nom_region']
    df = pd.read_csv('/Users/mosbahhachem/Documents/git/PROJET/Projet_file_rouge/departements-france.csv',
                                header=None, skiprows=[0], names=names)




    QUERY1['DEPARTEMENT'] = QUERY1['DEPARTEMENT'].astype('int')
    QUERY1 = QUERY1.sort_values(by='DEPARTEMENT', ascending = True)
    QUERY1['DEPARTEMENT']=QUERY1.DEPARTEMENT//10


    QUERY = pd.DataFrame(QUERY1['Nombre_usagers_accidentés'])
    df = pd.DataFrame(df[['code_departement','nom_departement','code_region', 'nom_region']])

    df2 = pd.concat([QUERY, df], axis =1)
# Creat figure
    fig = px.choropleth_mapbox(df2,geojson= geojson
                           ,color="Nombre_usagers_accidentés"
                           ,locations="code_departement"
                           ,featureidkey="properties.code"
                           ,hover_name = 'nom_departement'
                           , color_continuous_scale = [(0,"green"), (1,"red")]
                           #,color_continuous_midpoint = 2
                           ,range_color = (0, 2000)
                           #,title="NOMBRE TOTALE D'USAGERS ACCIDENTÉS PAR DEPARTEMENT" 
                           ,center={"lat": 46.3223, "lon": 1.2549}
                           ,mapbox_style="carto-positron", zoom=4.5)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    graphJSON = json.dumps (fig, cls = plotly.utils.PlotlyJSONEncoder) 
    
    return graphJSON