try:
    from pyfirmata import Arduino, util
except:
    from pip._internal.main import main
    main(['install','pyfirmata'])
    from pyfirmata import Arduino, util