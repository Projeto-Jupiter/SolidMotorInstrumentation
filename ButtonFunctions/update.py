import numpy as np

from connections import NoDataAvailableException


def update(application):
    for sensor in application.sensor_data:
        if sensor.updateStatus:
            try:
                sensor_connection = application.connection.get_handler(sensor.name)
                msg = sensor_connection.fetch_data()
                print(msg)
            except NoDataAvailableException:
                print('No data available')
                return
            pair = msg.split(",")
            if len(pair) == 2:
                time, pforce = pair
                # check data
                pforce = float(pforce)
                force = pforce
                time = float(time)
                sensor.data.append(force)
                sensor.times.append(time)
                application.plot_pannels[sensor.name].plot(sensor.times, sensor.data, clear=True, _callSync='off')

    #now = pg.ptime.time()
    #fps = 1.0 / (now - lastUpdate)
    #lastUpdate = now
    #avgFps = avgFps * 0.8 + fps * 0.2
    #application.label.setText("Generating %0.2f fps" % avgFps)

    # if rec:
    #    pforces.append(force)
    #    ptimes.append(time - t0)
    #    pydata = np.asarray(pforces)
    #    pxdata = np.asarray(ptimes)
    #    prplt.plot(pxdata, pydata, clear=True, _callSync='off')
