import flask
from flask import Flask, render_template, url_for, request
import pickle
import pandas as pd
import numpy as np

# initialize the app
app = Flask(__name__)

with open("../cos_dist.pkl", "rb") as f:
    df_cos = pickle.load(f)

with open("../man_dist.pkl", "rb") as f:
    df_man = pickle.load(f)

with open("../euc_dist.pkl", "rb") as f:
    df_euc = pickle.load(f)

with open("../friends_df.pkl", "rb") as f:
    df = pickle.load(f)


def top_5_recommended(episode, dist_metric='cosine'):
    if dist_metric == 'cosine':
        eps = df_cos.loc[episode].sort_values()[1:6].index.values
        script_links = []
        net_links = []
        for episode in eps:
            script_links.append(df[df['episode_name'] == episode]['script_link'].values[0])
            net_links.append(df[df['episode_name'] == episode]['netflix_link'].values[0])
        return list(zip(eps, net_links, script_links))
    elif dist_metric == 'manhattan':
        eps = df_man.loc[episode].sort_values()[1:6].index.values
        script_links = []
        net_links = []
        for episode in eps:
            script_links.append(df[df['episode_name'] == episode]['script_link'].values[0])
            net_links.append(df[df['episode_name'] == episode]['netflix_link'].values[0])
        return list(zip(eps, net_links, script_links))
    elif dist_metric == 'euclidean':
        eps = df_euc.loc[episode].sort_values()[1:6].index.values
        script_links = []
        net_links = []
        for episode in eps:
            script_links.append(df[df['episode_name'] == episode]['script_link'].values[0])
            net_links.append(df[df['episode_name'] == episode]['netflix_link'].values[0])
        return list(zip(eps, net_links, script_links))


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="I'll be there for you!")
#"I'll be there for you! test"


@app.route("/recommend", methods=['GET', 'POST'])
def recommend():

    episode = request.args.get('episode', 'Episode 101: The Pilot-The Uncut Version')
    distance_metric = request.args.get('distance', 'cosine')
    recommendation = top_5_recommended(episode, distance_metric)

    return render_template('recommend.html',
                           recommendation=recommendation,
                           episode=episode,
                           distance_metric=distance_metric)



# For local development:
app.run(debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
