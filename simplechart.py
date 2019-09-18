import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
import pandas as pd
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FileChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="FileChooser Example")
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            openx = dialog.get_filename()#Get the File name as a variable
            data = pd.read_excel(openx) # That funtion reads the archive and crete the dataframe
            data.drop(["ID", "Nome","Hora de início","Hora de conclusão","Email", 
            "Data de Nascimento", "Por que você prestou o Vestibular nesta faculdade?"], axis=1, inplace=True) # Adjusting the dataframe
            coluna = data.columns # Set the name of columns in an array
            plt.figure("Trabalho Sócio Econômico") # Set the name of the figure
            # Ploting all pie charts acording the name of column
            for i in coluna:
                data[i].value_counts().plot.pie(title= i, label=i, autopct='%1.1f%%',figsize=(16,9)) # Ploting a Pie Chart
                plt.ylabel('')
                plt.legend(title=i,loc="best") # Seting the Legend
                plt.show() # Showing the chart
            
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            openx = dialog.get_filename()
            print(openx)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

win = FileChooserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()