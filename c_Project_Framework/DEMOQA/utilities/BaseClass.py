import inspect
import pytest
import logging


@pytest.mark.usefixtures("setup")
class setting:
    pass
    


    def getLoggers(self):               #jgn lupa self -> agar bisa dipanggil login_test dgn self.getLoggers()
        loggername = inspect.stack()[1][3]  #< ikutin aja agar nama testcasenya bisa dimunculin di logfile
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s") #cek note diatas
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  #filehandler object

        logger.setLevel(logging.DEBUG)  #<< hirarci : akan print info sd kebawah critical, 
                                        #jika hanya warning maka yg dicetak di logfile : warning, error, critical
                                        #dst.
        return logger
    '''hirarki logger default :
    debug
    info
    warning
    error
    critical
     
    #sample message custom : 
    logger.debug("A debug statement is executed")
    logger.info("Information statement")            #jika setlevel dr sini, dgn kondisi level debug sblmnya ud diskip, mmaka
    logger.debug("A debug statement is executed")   #walaupun kita setlevel debug lg dibawah info tetap tdk akan tercetak level debug dibawah info ini
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")
    '''
    '''---------------------------------------------------------------------------------------------------------------------'''

       
    #bisa ditambah method2 spt:
    '''def VerifyLInkPresence(self,text):
    element = WebDriverWait(self.drv, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))
    )'''
    
    '''
    def SelectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
    '''

