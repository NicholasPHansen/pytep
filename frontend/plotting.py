import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import dash_html_components as html
import base64
import os

dummy_scatter = px.scatter(x=[1, 2, 3], y=[4, 5, 6])

eight_subplots = make_subplots(rows=4, cols=2, start_cell="bottom-left")
eight_subplots.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
eight_subplots.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=1, col=2)
eight_subplots.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]), row=2, col=1)
eight_subplots.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]), row=2, col=2)
eight_subplots.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=3, col=1)
eight_subplots.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=3, col=2)
eight_subplots.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]), row=4, col=1)
eight_subplots.add_trace(go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000]), row=4, col=2)
eight_subplots.update_yaxes(automargin=True)


three_subplots = make_subplots(rows=3, cols=1)
three_subplots.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
three_subplots.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=2, col=1)
three_subplots.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]), row=3, col=1)
three_subplots.update_yaxes(automargin=True)

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, '../dash_playground/fuckoff.png')
image_filename = file_path
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

middle_finger = html.Div([
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
], className="fitted-image")

