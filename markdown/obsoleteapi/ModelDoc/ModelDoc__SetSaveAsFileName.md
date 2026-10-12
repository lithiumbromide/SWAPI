---
title: "ModelDoc::SetSaveAsFileName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetSaveAsFileName.htm"
---

# ModelDoc::SetSaveAsFileName

This method is obsolete and has been superseded by [ModelDoc2::SetSaveAsFileName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetSaveAsFileName.htm).

Description

This method sets the Save As file name from within the FileSaveAsNotify2 event handlers, allowing the Solidworks file Save dialog to be bypassed.

Syntax (OLE Automation)

void ModelDoc.SetSaveAsFileName ( fileName )

| Input: | ( BSTR ) fileName | Filename to use |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SetSaveAsFileName ( fileName )

| Input: | ( BSTR ) fileName | Fielname to use |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use this method should from within the FileSaveAsNotify2 event handler. When setting the filename using this method, S_FALSE should be returned from the FileSaveAsNotify2 event handler. See AssemblyDoc::FileSaveAsNotify2, DrawingDoc::FileSaveAsNotify2, and PartDoc::FileSaveAsNotify2 notifications.
