
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': '',
    'last_name' : 'TRAORE',
    'address' : '中国',
    'job': '学生',
    'tel': '12345678925',
    'email': 'lfkh@yahoo.com',
    'description' : 'Suite à une expérience internationale en développement web et dans le domaine des arts, l’impact de l’intelligence artificielle dans nos vies me surprend de jour en jour. \n Aujourd’hui, je souhaite changer de cap et comprendre les secrets que recèlent nos données. J’aimerais mettre à profit ces découvertes au service des entreprises/associations à dimension sociale.',
    'social_media' : [
        {
            'link': 'https://www.facebook.com/nono',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences' : [
        {
            'title' : 'Web Developer',
            'company': 'AZULIK',
            'description' : 'Project manager and lead developer for several AZULIK websites.',
            'timeframe' : 'July 2018 - November 2019'
        },
        {
            'title' : 'Freelance Web Developer',
            'company': 'Independant',
            'description' : 'Create Wordpress websites for small and medium companies. ',
            'timeframe' : 'February 2017 - Present'
        },
        {
            'title' : 'Sharepoint Intern',
            'company': 'ALTEN',
            'description' : 'Help to manage a 600 Sharepoint sites platform (audit, migration to Sharepoint newer versions)',
            'timeframe' : 'October 2015 - October 2016'
        }
    ],
    'education' : [
        {
            'university': 'Paris Diderot',
            'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2015 - 2016'
        },
        {
            'university': 'Paris Dauphine',
            'degree': 'Master en Management global',
            'description' : 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
            'mention' : 'Bien',
            'timeframe' : '2015'
        },
        {
            'university': 'Lycée Turgot - Paris Sorbonne',
            'degree': 'CPGE Economie & Gestion',
            'description' : 'Préparation au concours de l\'ENS Cachan, section Economie',
            'mention' : 'N/A',
            'timeframe' : '2010 - 2012'
        }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['Dance', 'Travel', 'Languages']
}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))



@app.route('/chart')
def chart():
    return render_template('chartsajax.html', graphJSON=gm(),graphJSON1=gm1(),graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5())

#长条图strip
def gm():
    df = pd.read_csv('diamonds.csv')

    fig = px.strip(df, x="clarity", y="carat", color="cut")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
#条形图bar
def gm1(color="J"):
    df = pd.read_csv('diamonds.csv')

    fig = px.bar(df[df['color'] == color], x="clarity", y="carat", color="cut")

    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1
#散点图scatter
def gm2(clarity="IF"):
    df = pd.read_csv('diamonds.csv')

    fig=px.scatter(df[df['clarity']== clarity], x="price", y="color", color="cut")

    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2
#箱形图box
def gm3(clarity="IF"):
    df = pd.read_csv('diamonds.csv')

    fig = px.box(df[df['clarity']== clarity], x="cut", y="color")

    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3
#直方图histogram
def gm4(clarity="IF"):
    df = pd.read_csv('diamonds.csv')

    fig = px.histogram(df[df['clarity']== clarity], x="color", y="carat", color="cut")

    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON4
#堆积区域图area
def gm5(clarity="IF"):
    df = pd.read_csv('diamonds.csv')

    fig = px.area(df[df['clarity']== clarity], x="color", y="carat", color="cut")

    graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5


@app.route('/chart1')
def chart1():
    return render_template('chartsajax1.html', graphJSON=g(),graphJSON1=g1(),graphJSON2=g2(),graphJSON3=g3(),graphJSON4=g4(),graphJSON5=g5())

def g():
    tips =pd.DataFrame(px.data.tips())
    fig=px.strip(tips, x="total_bill", y="time", orientation="h", color="smoker")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def g1():
    tips = pd.DataFrame(px.data.tips())
    fig = px.bar(tips, x="sex", y="total_bill", color="smoker", barmode="group",
                  facet_row="time", facet_col="day", category_orders={"day": ["Thur",
                                                                              "Fri", "Sat", "Sun"],
                                                                      "time": ["Lunch", "Dinner"]})

    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

def g2():
    tips = pd.DataFrame(px.data.tips())
    fig = px.scatter(tips, x="total_bill", y="tip", facet_row="time", facet_col="day",
           color="smoker", trendline="ols",category_orders={"day": ["Thur",
           "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})

    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON2

def g3():
    tips = pd.DataFrame(px.data.tips())
    fig = px.parallel_categories(tips, color="size", color_continuous_scale=px.
            colors.sequential.Inferno)

    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON3

def g4():
    tips = pd.DataFrame(px.data.tips())
    fig = px.histogram(tips, x="sex", y="tip", histfunc="avg", color="smoker",
             barmode="group", facet_row="time", facet_col="day",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
             "time": ["Lunch", "Dinner"]})

    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON4

def g5():
    tips = pd.DataFrame(px.data.tips())
    fig = px.box(tips, x="day", y="total_bill", color="smoker", notched=True)

    graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON5


@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
