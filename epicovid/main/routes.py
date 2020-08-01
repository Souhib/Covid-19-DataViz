from flask import render_template, request, Blueprint
from epicovid.main.data import Data
from datetime import datetime
from epicovid.main.data_adapter import getConfirmedCasesByCountry, getTotalDeathsByCountry, getRecoveredByCountry, getChartsData
import json

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home/')
def home():
    """
    home

    Create a Chart and a Data object and return the home page template with Data object

    :return: render the template with data needed for the charts and the data containers
    :rtype: html template
    """
    dataConf = Data()
    chartsData = getChartsData()
    return render_template('home.html',
                           chartsData=chartsData, data=dataConf)


@main.route('/totalConfirmed/')
def totalConfirmed():
    """
    totalConfirmed

    Create a Data object and return the totalConfirmed page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    totalConfirmed = Data().getTotalConfirmed()
    return render_template('totalConfirmed.html', totalConfirmed=totalConfirmed)


@main.route('/confirmedCasesByCountry/')
def confirmedCasesByCountry():
    """
    confirmedCasesByCountry

    Create a Data object and return the confirmedCasesByCountry page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    confirmedCasesByCountry = getConfirmedCasesByCountry()
    return render_template('confirmedCasesByCountry.html', confirmedCasesByCountry=confirmedCasesByCountry)

@main.route('/totalDeaths/')
def totalDeaths():
    """
    totalDeaths

    Create a Data object and return the totalDeaths page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    totalDeath = Data().getTotalDeath()
    return render_template('totalDeaths.html', totalDeath=totalDeath)

@main.route('/deathsCasesByCountry/')
def deathsCasesByCountry():
    """
    deathsCasesByCountry

    Create a Data object and return the deathsCasesByCountry page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    deathsCasesByCountry = getTotalDeathsByCountry()
    return render_template('deathsCasesByCountry.html', deathsCasesByCountry=deathsCasesByCountry)

@main.route('/totalRecovered/')
def totalRecovered():
    """
    totalRecovered

    Create a Data object and return the totalRecovered page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    totalRecovered = Data().getTotalRecovered()
    return render_template('totalRecovered.html', totalRecovered=totalRecovered)

@main.route('/recoveredCasesByCountry/')
def recoveredCasesByCountry():
    """
    recoveredCasesByCountry

    Create a Data object and return the recoveredCasesByCountry page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    recoveredCasesByCountry = getRecoveredByCountry()
    return render_template('recoveredCasesByCountry.html', recoveredCasesByCountry=recoveredCasesByCountry)

@main.route('/charts/')
def charts():
    """
    charts

    Create a Chart object and return the charts page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    chartsData = getChartsData()
    return render_template('charts.html', chartsData=chartsData)

@main.route('/map/')
def map():
    """
    map

    Create a Data object and return the map page template with Data object

    :return: render the template with data needed for the data containers
    :rtype: html template
    """
    dataConf = Data()
    return render_template('map.html', data=dataConf)
