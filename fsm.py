from transitions.extensions import GraphMachine

LL = 0;

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '1' or text.lower() == 'USCS introduction'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '2' or 'symbol meaning'

    def is_going_to_start(self, update):
        text = update.message.text
        return text.lower() == '3' or 'start ro classify'

    def is_going_to_inorganic(self, update):
        text = update.message.text
        return text.lower() == 'inorganic'

    def is_going_to_L(self, update):
        text = update.message.text
        LL = int(text)
        return int(text) < 50

    def is_going_to_H(self, update):
        text = update.message.text
        LL = int(text)
        return int(text) >= 50

    def is_going_to_CL(self, update):
        text = update.message.text
        return (int(text) > 7) and (int(text) >= 0.73*(LL-20))

    def is_going_to_CLML(self, update):
        text = update.message.text
        return (int(text) <= 7) and (int(text) >= 4) and (int(text) >= 0.73*(LL-20))

    def is_going_to_ML(self, update):
        text = update.message.text
        return (int(text) < 4) or (int(text) < 0.73*(LL-20))

    def is_going_to_CH(self, update):
        text = update.message.text
        return int(text) >= 0.73*(LL-20)

    def is_going_to_MH(self, update):
        text = update.message.text
        return int(text) < 0.73*(LL-20)

    def is_going_to_organic(self, update):
        text = update.message.text
        return text.lower() == 'organic'

    def is_going_to_OL(self, update):
        text = update.message.text
        return int(text) < 50

    def is_going_to_OH(self, update):
        text = update.message.text
        return int(text) >= 50

    def on_enter_user(self, update): 
        update.message.reply_text("You can select what you want to know.Please enter the number or sentence.\n1.UCUS introduction\n2.Symbol meaning\n3.start to classify")

    def on_enter_state1(self, update):
        update.message.reply_text("USCS is Unified Soil Classification System.\nIt is used to classify soil for civil engineering by physical properties of soil.")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("L:low plasticity\nH:high plasticity\nM:milt\nC:clay\nO:organic")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_start(self, update):
        update.message.reply_text("Is the soil organic or inorganic?")
        
    def on_exit_start(self, update):
        print('Leaving start')

    def on_enter_inorganic(self, update):
        update.message.reply_text("What is the liquid limit?")
        
    def on_exit_inorganic(self, update):
        print('Leaving inorganic')

    def on_enter_L(self, update):
        update.message.reply_text("What is PI?")
        
    def on_exit_L(self, update):
        print('Leaving L')

    def on_enter_H(self, update):
        update.message.reply_text("What is PI?")
        
    def on_exit_H(self, update):
        print('Leaving H')

    def on_enter_CL(self, update):
        update.message.reply_text("The soil is CL.")
        self.go_back(update)
        
    def on_exit_CL(self, update):
        print('Leaving CL')

    def on_enter_CLML(self, update):
        update.message.reply_text("The soil is CL-ML.")
        self.go_back(update)
        
    def on_exit_CMLL(self, update):
        print('Leaving CLML')

    def on_enter_ML(self, update):
        update.message.reply_text("The soil is ML.")
        self.go_back(update)
        
    def on_exit_ML(self, update):
        print('Leaving ML')

    def on_enter_CH(self, update):
        update.message.reply_text("The soil is CH.")
        self.go_back(update)
        
    def on_exit_CH(self, update):
        print('Leaving CH')

    def on_enter_MH(self, update):
        update.message.reply_text("The soil is MH.")
        self.go_back(update)
        
    def on_exit_MH(self, update):
        print('Leaving MH')

    def on_enter_organic(self, update):
        update.message.reply_text("What is the liquid limit?")
        
    def on_exit_organic(self, update):
        print('Leaving organic')

    def on_enter_OL(self, update):
        update.message.reply_text("The soil is OL.")
        self.go_back(update)
        
    def on_exit_OL(self, update):
        print('Leaving OL')

    def on_enter_OH(self, update):
        update.message.reply_text("The soil is OH.")
        self.go_back(update)

    def on_exit_OH(self, update):
        print('Leaving OH')
