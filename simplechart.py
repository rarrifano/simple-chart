import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
import xlrd
import csv
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
            openx = dialog.get_filename()
            wb = xlrd.open_workbook(openx)
            sh = wb.sheet_by_index(0)
            file = open('file.csv', 'w',encoding='utf-8')
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    
            for rownum in range(sh.nrows):
                wr.writerow(sh.row_values(rownum))

            file.close()
            dialog.destroy()
            data = pd.read_csv('file.csv')
            data.drop(["ID", "Nome","Hora de início","Hora de conclusão","Email", 
            "Data de Nascimento", "Por que você prestou o Vestibular nesta faculdade?"], axis=1, inplace=True)
            coluna = data.columns
            plt.figure("Trabalho Sócio Econômico")
            #testa a geração do gráfico de acordo com as colunas
            for i in coluna:
                lablel = data[i].value_counts()
                data[i].value_counts().plot.pie(title= i, label=i, autopct='%1.1f%%',figsize=(16,9))
                plt.axis('equal')
                plt.tight_layout()
                plt.legend(title=i,loc="best" )

                plt.ylabel('')
                
                plt.show()
            
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