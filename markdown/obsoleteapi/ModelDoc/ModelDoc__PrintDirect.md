---
title: "ModelDoc::PrintDirect"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__PrintDirect.htm"
---

# ModelDoc::PrintDirect

This method is obsolete and has been superseded by [ModelDoc2::PrintDirect](sldworksAPI.chm::/ModelDoc2/ModelDoc2__PrintDirect.htm).

Description

This method prints the current document to the default printer.

Syntax (OLE Automation)

void ModelDoc.PrintDirect ()

Syntax (COM)

status = ModelDoc->PrintDirect ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

For a drawing document, all sheets are printed. For a part or assembly document, the currently active view is printed.
