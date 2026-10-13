---
title: "SldWorks::ActivePrinter"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__ActivePrinter.htm"
---

# SldWorks::ActivePrinter

This property is obsolete and has been superseded by [ModelDoc2::Printer](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Printer.htm).

Description

This property gets or sets the active SolidWorks printer.

Syntax (OLE Automation)

printer = SldWorks.ActivePrinter (VB Get property)

SldWorks.ActivePrinter = printer (VB Set property)

printer = SldWorks.GetActivePrinter ( ) (C++ Get property)

SldWorks.SetActivePrinter ( printer ) (C++ Set property)

| Property: | (BSTR) printer | Name of the printer |
| --- | --- | --- |

Syntax (Com)

status = SldWorks->get_ActivePrinter( &printer )

status = SldWorks->put_ActivePrinter( printer )

| Property: | (BSTR) printer | Name of the printer |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
