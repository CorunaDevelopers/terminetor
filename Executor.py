class LocalExecutor():

    def execute(self, command):


        bool = False
        if (command == 'on'):
            print('Execute on')
            bool = True
        elif (command == 'off'):
            print('Execute off')
            bool = True
        return bool
