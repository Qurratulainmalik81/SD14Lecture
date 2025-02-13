# Description: The St. John’s Marina & Yacht Club 
# Author: Cameron Boyer
# Date(s): Jan 24, 2025 - Feb 1, 2025
 
 

# Define program constants.

ALT_MEM_COST    = 5.00    # Cost per Alternate Member
SITE_CLEAN_COST = 50.00   # Site Cleaning Fee
VIDEO_SUR_COST  = 35.00   # Video Surveillance Fee
STAN_MEM_COST   = 75.00   # Standard Member Cost
EXCL_MEM_COST   = 150.00  # Exclusive Member Cost
PROCESS_COST    = 59.99   # Initial Processing Fee

CANCEL_RATE  = .60  # Cancellation Fee Rate
HST_RATE     = .15  # Sales Tax Rate

 
# Main program starts here.
 
   
# Gather user inputs.

CurDate = input("Enter the current date (YYYY-MM-DD): ")
SiteNum = int(input("Enter the site number (1-100): ")) 

MemName   = input("Enter client name: ")
StAdd     = input("Enter client street address: ")
City      = input("Enter client city: ")
Prov      = input("Enter client province (XX): ").upper()
PostCode  = input("Enter client postal code: ").upper()
HomePhone = input("Enter client home phone number (XXXXXXXXXX): ")
CellPhone = input("Enter client cell number (XXXXXXXXXX): ")

MemType    = input("Enter member type (S / E): ").upper()
NumAltMem  = int(input("Enter number of alternate members: "))

SiteClean = input("Site cleaning service (Y / N): ").upper()
VideoSur  = input("Site video surveillance (Y / N):  ").upper()


# Perform required calculations.
 
if SiteNum % 2 == 0:  # if the site number is divisible by 2 (an even number) 
    SiteCost = 80.00
else:
    SiteCost = 120.00

if SiteClean == "Y":
    SiteCleanCost = SITE_CLEAN_COST
else: 
    SiteCleanCost = 0

if VideoSur == "Y":
    VideoSurCost = VIDEO_SUR_COST
else: 
    VideoSurCost = 0
 
SiteCharge  =  SiteCost + (NumAltMem * ALT_MEM_COST) 
ExtraCharge = SiteCleanCost + VideoSurCost

SubTotal = SiteCharge + ExtraCharge
HST      = SubTotal * HST_RATE

TotMonthCharge = SubTotal + HST

if MemType == "S":
    MonthDues = STAN_MEM_COST
else:
    MonthDues = EXCL_MEM_COST

TotMonthFee = TotMonthCharge + MonthDues
YearlyFee   = TotMonthFee * 12

MonthPay = (YearlyFee + PROCESS_COST) / 12

CancelFee = (SiteCharge * 12) * CANCEL_RATE


# Display results

print()
print(f"     St. John's Marina & Yacht Club ")
print(f"          Yearly Member Receipt")
print()
print(f"----------------------------------------")
print()
print(f"Client Name and Address:")
print()
print(f"{MemName:<24s}")
print(f"{StAdd:<24s}")
print(f"{City}, {Prov:<2s}  {PostCode:<6s}")
print()
print(f"Phone: {HomePhone:<10s}(H)")
print(f"       {CellPhone:<10s}(C)")
print()
if MemType == "S":
    MemType = "Standard"
else:
    MemType = "Exclusive"
print(f"Site#: {SiteNum:0>3d}        Member type: {MemType:>9s}")
print()
print(f"Alternate members:                    {NumAltMem:>2d}")
if SiteClean == "Y":
    SiteClean = "Yes"
else:
    SiteClean = "No"
print(f"Weekly site cleaning:                {SiteClean:>3s}")
if VideoSur == "Y":
    VideoSur = "Yes"
else:
    VideoSur = "No"
print(f"Video Surveillance:                  {VideoSur:>3s}")
print()
SiteChargeDsp = "${:,.2f}".format(SiteCharge)
print(f"Site charges:                  {SiteChargeDsp:>9s}")
ExtraChargeDsp = "${:,.2f}".format(ExtraCharge)
print(f"Extra charges:                 {ExtraChargeDsp:>9s}")
print(f"                              ----------")
SubTotalDsp = "${:,.2f}".format(SubTotal)
print(f"Subtotal:                      {SubTotalDsp:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f"Sales tax (HST):               {HSTDsp:>9s}")
print(f"                              ----------")
TotMonthChargeDsp = "${:,.2f}".format(TotMonthCharge)
print(f"Total monthly charges:         {TotMonthChargeDsp:>9s}")
MonthDuesDsp = "${:,.2f}".format(MonthDues)
print(f"Monthly dues:                  {MonthDuesDsp:>9s}")
print(f"                              ----------")
TotMonthFeeDsp = "${:,.2f}".format(TotMonthFee)
print(f"Total monthly fees:            {TotMonthFeeDsp:>9s}")
YearlyFeeDsp = "${:,.2f}".format(YearlyFee)
print(f"Total yearly fee:             {YearlyFeeDsp:>10s}")
print()
MonthPayDsp = "${:,.2f}".format(MonthPay)
print(f"Monthly payment:               {MonthPayDsp:>9s}")
print()
print(f"----------------------------------------")
print()
print(f"Issued: {CurDate:<10s}")
print(f"HST Reg No: 549-33-5849-4720-9885")
print()
CancelFeeDsp = "${:,.2f}".format(CancelFee)
print(f"Cancellation fee:              {CancelFeeDsp:>9s}")
