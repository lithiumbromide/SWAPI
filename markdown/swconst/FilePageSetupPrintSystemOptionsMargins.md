---
title: "File > Print > Margins"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FilePageSetupPrintSystemOptionsMargins.htm"
---

# File > Print > Margins

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Paper margins - Top | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterTopMargin) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterTopMargin, < Value >) | Double value in meters | Specifies width of left margin |
| Paper margins - Bottom | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterBottomMargin) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterBottomMargin, < Value >) | Double value in meters | Specifies width of left margin |
| Paper margins - Left | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterLeftMargin) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterLeftMargin, < Value >) | Double value in meters | Specifies width of left margin |
| Paper margins - Right | ISldWorks::GetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterRightMargin) ISldWorks::SetUserPreferenceDoubleValue (swUserPreferenceDoubleValue_e.swPageSetupPrinterRightMargin, < Value >) | Double value in meters | Specifies width of left margin |
| Paper margins - Use printer's margins | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupPrinterUsePrinterMargin) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swPageSetupPrinterUsePrinterMargin, < OnFlag >) | Boolean value | Specifies whether to print document with printer's default margin values |
