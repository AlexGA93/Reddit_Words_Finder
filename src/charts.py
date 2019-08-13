
import plotly.graph_objects as go


'''
data = [
    ['popular', 'all', 'CAguns'],
    ['and', 'is', 'but', 'if', 'me'],
    [26, 46, 60, 70, 79]
]'''


def plotMethod(subr, words, num, value):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=num,
        theta=words,
        fill='toself',
        name='Similarities Found'
    ))

    fig.update_layout(

        title=go.layout.Title(
            text="Subreddits similarities found in: %s  " % (subr),
            xref="paper",
            x=0),

        polar=dict(radialaxis=dict(
            visible=True, range=[0, value])), showlegend=False
    )

    fig.show()


def main(data):
    dataSubr = data[0]
    dataWords = data[1]
    dataNum = data[2]  # coun array
    value = 0
    # highest value for dataNum
    for i in dataNum:
        if i > value:
            value = i

    plotMethod(dataSubr, dataWords, dataNum, value)
