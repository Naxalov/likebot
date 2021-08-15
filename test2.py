appointment1 = { 'soccer' : {
                        'day' : 20,
                       'month' : 'april'
                       }

            }
appointment2 = { 'soccer' : {
                        'day' : 20,
                        'month' : 'april'
                       },
              'gym' : {
                        'day' : 5,
                        'month' : 'may'
                       }
            }
appointment = {**appointment1,**appointment2}

print(appointment)