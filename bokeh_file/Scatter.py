from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.transform import factor_cmap, factor_mark
from bokeh.models import AjaxDataSource
def show_scatter():
    # output to static HTML file
    output_file("line.html")

    p = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

    # show the results
    show(p)


def show_square():
    # output to static HTML file
    output_file("square.html")

    p = figure(plot_width=400, plot_height=400)

    # add a square renderer with a size, color, and alpha
    p.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="olive", alpha=0.5)

    # show the results
    show(p)

def mapping_marker():
    SPECIES = ['setosa', 'versicolor', 'virginica']
    MARKERS = ['hex', 'circle_x', 'triangle']

    p = figure(title="Iris Morphology")
    p.xaxis.axis_label = 'Petal Length'
    p.yaxis.axis_label = 'Sepal Width'

    p.scatter("petal_length", "sepal_width", source=flowers, legend_field="species", fill_alpha=0.4, size=12,
              marker=factor_mark('species', MARKERS, SPECIES),
              color=factor_cmap('species', 'Category10_3', SPECIES))

    show(p)


def ajax_data_sample():
    # setup AjaxDataSource with URL and polling interval
    source = AjaxDataSource(data_url='http://some.api.com/data',
                            polling_interval=100)
    p = figure()

    # use the AjaxDataSource just like a ColumnDataSource
    p.circle('x', 'y', source=source)
    show(p)