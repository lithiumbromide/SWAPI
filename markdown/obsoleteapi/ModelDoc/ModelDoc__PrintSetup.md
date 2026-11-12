---
title: "ModelDoc::PrintSetup"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__PrintSetup.htm"
---

# ModelDoc::PrintSetup

This method is obsolete. Use [ModelDoc2::SetUserPreferenceDoubleValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceDoubleValue.htm), [ModelDoc2::SetUserPreferenceIntegerValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceIntegerValue.htm), and [ModelDoc2::SetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceToggle.htm).

Description

This property gets and sets various parameters for the current SolidWorks printer. The current SolidWorks printer can be determined or changed by calling ModelDoc::ActivePrinter.

Syntax (OLE Automation)

setupValue = ModelDoc.PrintSetup(setupType) (VB Get property)

ModelDoc.PrintSetup(setupType) = setupValue (VB Set property)

setupValue = ModelDoc.GetPrintSetup ( setupType ) (C++ Get property)

ModelDoc.SetPrintSetup ( setupType, setupValue ) (C++ Set property)

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |

Syntax (Com)

status = ModelDoc->get_PrintSetup( setupType, &setupValue )

status = ModelDoc->put_PrintSetup( setupType, setupValue )

| Input: | (long)setupType | Type of property to set as defined in swPrintProperties_e. |
| --- | --- | --- |
| Property: | (int) setupValue | Value for property |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

For information about values for the argument setupValue, see Visual Basic online Help topics about printer object constraints.
