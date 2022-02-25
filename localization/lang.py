from localization.th import TH
from localization.en import EN

LANGUAGEs = "EN"
def change_lang(LANGUAGEs):
    if LANGUAGEs == "TH":
        LOCALs = TH
    if LANGUAGEs == "EN":
        LOCALs = EN
    return LOCALs
LOCALs = change_lang(LANGUAGEs)
LOCALs["version"] = "4.1"