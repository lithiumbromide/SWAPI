---
title: "ModelDoc::PrintOut2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__PrintOut2.htm"
---

# ModelDoc::PrintOut2

This method is obsolete and has been superseded by [ModelDoc2::PrintOut2](../ModelDoc2/ModelDoc2__PrintOut2.htm).

Description

This method prints a document.

Syntax (OLE Automation)

void ModelDoc.PrintOut2 ( fromPage, toPage, numCopies, collate, printer, scale, printToFile, printFileName)

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (BOOL) collate | TRUE if you wish to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Name of the printer queue name.; if you pass a NULL string, then the document prints the current SolidWorks printer; the current SolidWorks printers can be set using the SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale in decimal form; to print the document at 50%, pass 0.5; to print at 200%, pass 2.0; if you pass 0.0, then your document is scaled to fit the page |
| Input: | (BOOL) printToFile | TRUE if you want to print to a file; this will print to the file specified in the printFileName argument |
| Input: | (BSTR) printFileName | Name of the file to which to print if PrintToFile is TRUE |

Syntax (COM)

status = ModelDoc->PrintOut2 ( fromPage, toPage, numCopies, collate, printer, scale, printToFile, printFileName)

| Input: | (long) fromPage | First page in the range to be printed |
| --- | --- | --- |
| Input: | (long) toPage | Last page in the range to be printed |
| Input: | (long) numCopies | Number of copies to print |
| Input: | (VARIANT_BOOL) collate | TRUE if you wish to collate the copies, FALSE otherwise |
| Input: | (BSTR) printer | Name of the printer queue name.; if you pass a NULL string, then the document prints the current SolidWorks printer; the current SolidWorks printers can be set using the SldWorks::ActivePrinter property |
| Input: | (double) scale | Scale in decimal form; to print the document at 50%, pass 0.5; to print at 200%, pass 2.0; if you pass 0.0, then your document is scaled to fit the page |
| Input: | (VARIANT_BOOL) printToFile | TRUE if you want to print to a file; this will print to the file specified in the printFileName argument |
| Input: | (BSTR) printFileName | Name of the file to which to print if PrintToFile is TRUE |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

It is recommended that you pass a NULL string for the name of the printer queue name and set the active printer using the SldWorks::ActivePrinter property. If you pass an actual value for the printer parameter, then this method only uses the eight specified parameters and ignores any settings you have made using ModelDoc::PrintSetup. If you set the active printer using SldWorks::ActivePrinter and then pass a NULL string to the printer argument, then calls to ModelDoc::PrintSetup are recognized by this method.

Printing to a file may be done without the standard Microsoft Print To dialog appearing.
