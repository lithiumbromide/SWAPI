---
title: "ModelDoc2::PrintSetup"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__PrintSetup.htm"
---

# ModelDoc2::PrintSetup

This method is obsolete and has been superseded by [ModelDoc2::SetUserPreferenceDoubleValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceDoubleValue.htm), [ModelDoc2::SetUserPreferenceIntegerValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceIntegerValue.htm), and [ModelDoc2::SetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceToggle.htm).

Description

This property gets and sets various parameters for the current SolidWorks printer.

Syntax (OLE Automation)

setupValue = ModelDoc2.PrintSetup(setupType) (VB Get property)

ModelDoc2.PrintSetup(setupType) = setupValue (VB Set property)

setupValue = ModelDoc2.GetPrintSetup ( setupType ) (C++ Get property)

ModelDoc2.SetPrintSetup ( setupType, setupValue ) (C++ Set property)

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |

Syntax (Com)

status = ModelDoc2->get_PrintSetup( setupType, &setupValue )

status = ModelDoc2->put_PrintSetup( setupType, setupValue )

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use SldWorks::ActivePrinter to determine or change the current SolidWorks printer.

For information about values for the argument setupValue, see the MSDEV or Visual Basic Help.
