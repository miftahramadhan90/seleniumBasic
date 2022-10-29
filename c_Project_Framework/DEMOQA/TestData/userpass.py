
class LoginData:
    
    login_valid = [{'username':'idejongkok', 'password':'asDF12#$'}]

    login_invalid = [{'username':'idejongkok', 'password':'asaa'},  # user benar, pass salah - 4 
                        {'username':'asaa', 'password':'asDF12#$'},          # user salah, pass benar - 8
                        {'username':'asaaa', 'password':'asaaaa'}
                        ]