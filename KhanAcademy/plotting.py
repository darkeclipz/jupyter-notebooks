import plotly
plotly.offline.init_notebook_mode()

def plot_line_fixed(x,y, title_x='', title_y='', d=[0,1]):
    trace = plotly.graph_objs.Scatter(
        x = x,
        y = y
    )
    layout = dict(
        xaxis = dict(title=title_x,domain=d),
        yaxis = dict(title=title_y,scaleanchor='x',scaleratio=1,domain=d),
    )
    data = [trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.iplot(fig, filename='line')

def plot_2d_fixed(x,y,z=[], title_x='', title_y='',d=[0,1]):
    trace = plotly.graph_objs.Scatter(
        x = x,
        y = y,
        mode = 'markers+text',
        name = 'Name',
        text = z,
        marker = dict(size=16,line=dict(width=2,color='rgba(0,0,0,.4)'), color='rgba(100,100,100,0.3)'),
        textposition='top'
    )
    layout = plotly.graph_objs.Layout(
        hovermode='closest',        
        xaxis=dict(
            title=title_x,
            domain=d
        ),
        yaxis=dict(
            title=title_y,
            scaleanchor='x',
            scaleratio=1,
            domain=d
        ),
        showlegend = False
    )
    data = [trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.iplot(fig, filename='line')

def plot_line(x,y, title_x='', title_y=''):
    trace = plotly.graph_objs.Scatter(
        x = x,
        y = y
    )
    layout = dict(
        xaxis = dict(title=title_x),
        yaxis = dict(title=title_y),
    )
    data = [trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.iplot(fig, filename='line')

def plot_2d(x,y,z=[], title_x='', title_y=''):
    trace = plotly.graph_objs.Scatter(
        x = x,
        y = y,
        mode = 'markers+text',
        name = 'Name',
        text = z,
        marker = dict(size=16,line=dict(width=2,color='rgba(0,0,0,.4)'), color='rgba(100,100,100,0.3)'),
        textposition='top'
    )
    layout = plotly.graph_objs.Layout(
        hovermode='closest',        
        xaxis=dict(
            title=title_x,
        ),
        yaxis=dict(
            title=title_y,
        ),
        showlegend = False
    )
    data = [trace]
    fig = dict(data=data, layout=layout)
    plotly.offline.iplot(fig, filename='line')
