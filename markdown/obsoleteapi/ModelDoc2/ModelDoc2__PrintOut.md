---
title: "ModelDoc2::PrintOut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__PrintOut.htm"
---

# ModelDoc2::PrintOut

This method is obsolete and has been superseded by [ModelDoc2::PrintOut2](ModelDoc2__PrintOut2.htm).

Description

This method prints a document.

Syntax (OLE Automation)

void ModelDoc2.PrintOut ( fromPage, toPage, numCopies, collate, printer, scale, printToFile)

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (BOOL) collate | TRUE to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Printer queue name; if you pass a NULL string, then the document goes to the default SolidWorks printer; set up SolidWorks printers using the SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale, in decimal form To print the document... Then pass... At 50% its size 0.5 At 200% its size 2.0 To fit the page 0.0 |
| To print the document... | Then pass... |  |
| At 50% its size | 0.5 |  |
| At 200% its size | 2.0 |  |
| To fit the page | 0.0 |  |
| Input: | (BOOL) printToFile | TRUE to print to a file; A dialog appears for end-user to fill in |

Syntax (COM)

status = ModelDoc2->PrintOut ( fromPage, toPage, numCopies, collate, printer, scale, printToFile )

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (VARIANT_BOOL) collate | TRUE to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Printer queue name; if you pass a NULL string, then the document goes to the default SolidWorks printer; set up SolidWorks printers using the SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale, in decimal form To print the document... Then pass... At 50% its size 0.5 At 200% its size 2.0 To fit the page 0.0 |
| To print the document... | Then pass... |  |
| At 50% its size | 0.5 |  |
| At 200% its size | 2.0 |  |
| To fit the page | 0.0 |  |
| Input: | (VARIANT_BOOL) printToFile | TRUE to print to a file; a dialog appears for the end-user to fill in |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

It is recommended that you set the active printer using the SldWorks::ActivePrinter property and pass a NULL string for the printer queue name in this method .

| If you... | Then... |
| --- | --- |
| Pass an actual value for the printer argument | This method uses only the specified arguments and ignores any settings set using ModelDoc2::PrintSetup. |
| set the active printer using ModelDoc2::Printer and then pass a NULL string to the printer argument | Calls to ModelDoc2::PrintSetup are recognized by this method |

NOTE: If you do not want the dialog to appear and you want to print the document to a file, then use ModelDoc2.PrintOut2.
