import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,QLabel, \
QPushButton, QTabWidget, QRadioButton, QGridLayout, QButtonGroup, \
QMessageBox
from Units import Kilometer, Meter, Feet, Inch, Litre, Millilitre, \
FluidOunce, Kilogram, Pound

class UnitConverter(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
    
        self.tab = QTabWidget(self)
        
        # Length Tab
        self.length = QWidget()
        
        self.lengthLabel = QLabel("Length Converter")
        self.lengthFrom = QLineEdit()
        self.lengthTo = QLineEdit()
        self.kilometersFrom = QRadioButton('Km',self)
        self.kilometersTo = QRadioButton('Km',self)
        self.metersFrom = QRadioButton('m', self)
        self.metersTo = QRadioButton('m', self)
        self.feetFrom = QRadioButton('ft', self)
        self.feetTo = QRadioButton('ft',self)
        self.inchesFrom = QRadioButton('in', self)
        self.inchesTo = QRadioButton('in', self)
        
        self.lengthButton = QPushButton("Convert")
        self.lengthButton.clicked.connect(self.convertLength)
        
        self.groupLength = QButtonGroup()
        self.groupLength.addButton(self.kilometersFrom)
        self.groupLength.addButton(self.kilometersTo)
        self.groupLength.addButton(self.metersFrom)
        self.groupLength.addButton(self.metersTo)
        self.groupLength.addButton(self.feetFrom)
        self.groupLength.addButton(self.feetTo)
        self.groupLength.addButton(self.inchesFrom)
        self.groupLength.addButton(self.inchesTo)
        self.groupLength.setExclusive(False)
        
        self.gridLength = QGridLayout()
        
        self.gridLength.addWidget(self.lengthLabel,0,1)
        self.gridLength.addWidget(self.lengthFrom,1,1)
        self.gridLength.addWidget(self.lengthTo,1,2)
        self.gridLength.addWidget(self.kilometersFrom,2,1)
        self.gridLength.addWidget(self.kilometersTo,2,2)
        self.gridLength.addWidget(self.metersFrom,3,1)
        self.gridLength.addWidget(self.metersTo,3,2)
        self.gridLength.addWidget(self.feetFrom,4,1)
        self.gridLength.addWidget(self.feetTo,4,2)
        self.gridLength.addWidget(self.inchesFrom,5,1)
        self.gridLength.addWidget(self.inchesTo,5,2)
        self.gridLength.addWidget(self.lengthButton,6,2)
        
        self.length.setLayout(self.gridLength)
        
        # Volume Tab
        self.volume = QWidget()
        
        self.volumeLabel = QLabel("Volume Converter")
        self.volumeFrom = QLineEdit()
        self.volumeTo = QLineEdit()
        self.litresFrom = QRadioButton('L',self)
        self.litresTo = QRadioButton('L', self)
        self.millilitresFrom = QRadioButton('mL', self)
        self.millilitresTo = QRadioButton('mL', self)
        self.fluidOuncesFrom = QRadioButton('fl oz', self)
        self.fluidOuncesTo = QRadioButton('fl oz', self) 
        
        self.volumeButton = QPushButton("Convert")
        self.volumeButton.clicked.connect(self.convertVolume)        
        
        self.groupVolume = QButtonGroup()
        self.groupVolume.addButton(self.litresFrom)
        self.groupVolume.addButton(self.litresTo)
        self.groupVolume.addButton(self.millilitresFrom)
        self.groupVolume.addButton(self.millilitresTo)
        self.groupVolume.addButton(self.fluidOuncesFrom)
        self.groupVolume.addButton(self.fluidOuncesTo)
        self.groupVolume.setExclusive(False)
        
        self.gridVolume = QGridLayout()
        
        self.gridVolume.addWidget(self.volumeLabel,0,1)
        self.gridVolume.addWidget(self.volumeFrom,1,1)
        self.gridVolume.addWidget(self.volumeTo,1,2)
        self.gridVolume.addWidget(self.litresFrom,2,1)
        self.gridVolume.addWidget(self.litresTo,2,2)
        self.gridVolume.addWidget(self.millilitresFrom,3,1)
        self.gridVolume.addWidget(self.millilitresTo,3,2)
        self.gridVolume.addWidget(self.fluidOuncesFrom,4,1)
        self.gridVolume.addWidget(self.fluidOuncesTo,4,2)
        self.gridVolume.addWidget(self.volumeButton,5,2)
        
        self.volume.setLayout(self.gridVolume)
        
        # Weight Tab
        self.weight = QWidget()
        
        self.weightLabel = QLabel("Weight Converter")
        self.weightFrom = QLineEdit()
        self.weightTo = QLineEdit()
        self.poundsFrom = QRadioButton('lbs',self)
        self.poundsTo = QRadioButton('lbs', self)
        self.kilogramFrom = QRadioButton('kg', self)
        self.kilogramTo = QRadioButton('kg', self)
        
        self.weightButton = QPushButton("Convert")
        self.weightButton.clicked.connect(self.convertWeight)
        
        self.groupWeight = QButtonGroup()
        self.groupWeight.addButton(self.poundsFrom)
        self.groupWeight.addButton(self.poundsTo)
        self.groupWeight.addButton(self.kilogramFrom)
        self.groupWeight.addButton(self.kilogramTo)
        self.groupWeight.setExclusive(False)
        
        self.gridWeight = QGridLayout()
        
        self.gridWeight.addWidget(self.weightLabel,0,1)
        self.gridWeight.addWidget(self.weightFrom,1,1)
        self.gridWeight.addWidget(self.weightTo,1,2)
        self.gridWeight.addWidget(self.poundsFrom,2,1)
        self.gridWeight.addWidget(self.poundsTo,2,2)
        self.gridWeight.addWidget(self.kilogramFrom,3,1)
        self.gridWeight.addWidget(self.kilogramTo,3,2)
        self.gridWeight.addWidget(self.weightButton,4,2)
        
        self.weight.setLayout(self.gridWeight)
        
        self.tab.addTab(self.length,"Length")
        self.tab.addTab(self.volume,"Volume")
        self.tab.addTab(self.weight, "Weight")
        
    
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Unit Converter')
        self.show()
    
    def convertLength(self):
        self.quantity = int(self.lengthFrom.text())
        
        if self.kilometersFrom.isChecked():
            km = Kilometer("Kilometer","km",self.quantity,"Length")
            if self.kilometersTo.isChecked():
                message = QMessageBox.warning(self,"Warning", "Can't convert km to km")
            elif self.metersTo.isChecked():
                converted = km.convert_to("meter",km.magnitude)
                self.lengthTo.setText(str(converted))
            elif self.feetTo.isChecked():
                converted = km.convert_to("feet",km.magnitude)
                self.lengthTo.setText(str(converted))
            elif self.inchesTo.isChecked():
                converted = km.convert_to("inches",km.magnitude)
                self.lengthTo.setText(str(converted))
        
        if self.metersFrom.isChecked():
            m = Meter("Meter", "m", self.quantity,"Length")
            if self.metersTo.isChecked():
                message = QMessageBox.warning(self, "Warning", "Can't convert m to m")
            elif self.kilometersTo.isChecked():
                converted = m.convert_to("kilometer",m.magnitude)
                self.lengthTo.setText(str(converted))
            elif self.feetTo.isChecked():
                converted = m.convert_to("feet",m.magnitude) 
                self.lengthTo.setText(str(converted))
            elif self.inchesTo.isChecked():
                converted = m.convert_to("inches",m.magnitude)
                self.lengthTo.setText(str(converted))

        if self.feetFrom.isChecked():
            ft = Feet("Feet", "ft", self.quantity, "Length")
            if self.feetTo.isChecked():
                message = QMessageBox.warning(self, "Warning", "Can't convert ft to ft")
            elif self.kilometersTo.isChecked():
                converted = ft.convert_to("kilometer",ft.magnitude)  
                self.lengthTo.setText(str(converted))
            elif self.metersTo.isChecked():
                converted = ft.convert_to("meter",ft.magnitude)
                self.lengthTo.setText(str(converted))
            elif self.inchesTo.isChecked():
                converted = ft.convert_to("inches",ft.magnitude)  
                self.lengthTo.setText(str(converted))  

        if self.inchesFrom.isChecked():
            inch = Inch("Inches", "in", self.quantity, "Length")
            if self.inchesTo.isChecked():
                message = QMessageBox.warning(self, "Warning", "Can't convert in to in")
            elif self.kilometersTo.isChecked():
                converted = inches.convert_to("kilometer",inches.magnitude) 
                self.lengthTo.setText(str(converted))
            elif self.metersTo.isChecked():
                converted = inches.convert_to("meters",inches.magnitude)
                self.lengthTo.setText(str(converted))
            elif self.feetTo.isChecked():
                converted = inches.convert_to("feet",inches.magnitude) 
                self.lengthTo.setText(str(converted))
    
    def convertVolume(self):
        self.quantity = int(self.volumeFrom.text())
        
        if self.litresFrom.isChecked():
            L = Litre("Litre", "L", self.quantity, "Volume")
            if self.litresTo.isChecked():
                message = QMessageBox.warning(self, "Warning", "Can't convert L to L")
            elif self.millilitresTo.isChecked():
                converted = L.convert_to("millilitres",L.magnitude)
                self.volumeTo.setText(str(converted))
            elif self.fluidOuncesTo.isChecked():
                converted = km.convert_to("fluid ounce",L.magnitude)
                self.volumeTo.setText(str(converted))
                
        if self.millilitresFrom.isChecked():
            mL = Millilitre("Millilitre", "mL", self.quantity, "Volume")
            if self.millilitresTo.isChecked():
                message = QMessageBox.warning(self, "Warning", "Can't convert mL to mL")
            elif self.litresTo.isChecked():
                converted = mL.convert_to("litre",mL.magnitude)
                self.volumeTo.setText(str(converted))
            elif self.fluidOuncesTo.isChecked():
                converted = mL.convert_to("fluid ounce",mL.magnitude)
                self.volumeTo.setText(str(converted))
                
        if self.fluidOuncesFrom.isChecked():
            flOz = FluidOunce("Fluid Ounce", "fl oz", self.quantity, "Volume")
            if self.fluidOuncesTo.isChecked():
                message = QMessageBox.warning(self, "Warning", "Can't convert fl oz to fl oz")
            elif self.litresTo.isChecked():
                converted = flOz.convert_to("litre",flOz.magnitude)
                self.volumeTo.setText(str(converted))
            elif self.millilitresTo.isChecked():
                converted = flOz.convert_to("millilitre",flOz.magnitude)
                self.volumeTo.setText(str(converted))
                
    def convertWeight(self):
        self.quantity = int(self.weightFrom.text())

        if self.kilogramFrom.isChecked():
            kg = Kilogram("Kilogram", "kg", self.quantity,"Weight")
            if self.kilogramTo.isChecked():
                message = QMessageBox.warning(self, "Warning", "Can't convert kg to kg")
            elif self.poundsTo.isChecked():
                converted = kg.convert_to("pound",kg.magnitude)
                self.weightTo.setText(str(converted))

        if self.poundsFrom.isChecked():
            lbs = Pound("Pound", "lbs", self.quantity, "Weight")
            if self.poundsTo.isChecked():
                message = QMessageBox.warning(self,"Warning", "Can't convert lbs to lbs")
            elif self.kilogramTo.isChecked():
                converted = lbs.convert_to("kilogram",lbs.magnitude)
                self.weightTo.setText(str(converted))                
if __name__ == '__main__':            
    app = QApplication(sys.argv)
    uc = UnitConverter()
    sys.exit(app.exec_())