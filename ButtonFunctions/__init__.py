import csv


def ignition(application):
    application.connection.write("sup\r\n")


def supress(application):
    application.connection.write("fire\r\n")


def save_curve(application) -> None:
    """Save Curve.

    Saves a curve into a csv format.
    """
    file_path = 'data.csv'
    with open(file_path, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(application.times)
        wr.writerow(application.forces)

def reset(application):
    #application.connection.reset()
    application.forces = []
    application.times = []
    application.plot_pannels['plot2'].clear()


def start_transducer(application):
    application.connection.write("fetchp\r\n")
    
def start_cell(application):
    application.update_cell = True

def stop_cell(application):
    application.update_cell = False