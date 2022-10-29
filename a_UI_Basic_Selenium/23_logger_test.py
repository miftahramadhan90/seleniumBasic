
''' Catantan -> logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
%(asctime)s     : timestampnya
%(levelname)s   : level loggernya (debug, info, warning, error, critical
%(name)s        : nama testcase nya -> test_xxx
%(message)s     : message yg sdh disetting di dalam masing2 level argumennya-> logger.error("pesannya xxxx")
'''
import logging

def test_logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s") #cek note diatas
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.INFO)  #<< hirarci : akan print info sd kebawah critical, 
                                    #jika hanya warning maka yg dicetak di logfile : warning, error, critical
                                    #dst.
    
    #------------custome message---, jika tidak dipakai akan pakai default/actual message :

    logger.debug("A debug statement is executed")
    logger.info("Information statement")            #jika setlevel dr sini, dgn kondisi level debug sblmnya ud diskip, mmaka
    logger.debug("A debug statement is executed")   #walaupun kita setlevel debug lg dibawah info tetap tdk akan tercetak level debug dibawah info ini
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")

    '''hirarki default :
    debug
    info
    warning
    error
    critical
    '''
    



