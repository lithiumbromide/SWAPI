---
title: "ModelDoc::SaveSilent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveSilent.htm"
---

# ModelDoc::SaveSilent

This method is obsolete and has been superseded by [ModelDoc::Save2](ModelDoc__Save2.htm).

Description

This method saves the current document with the current name. If it is a new document, use ModelDoc::SaveAsSilent instead. Dialog boxes are suppressed.

Syntax (OLE Automation)

Errors= ModelDoc.SaveSilent ( )

| Return: | (long) Errors | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->SaveSilent ( &Errors)

| Output: | (long) Errors | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to ModelDoc::Save except that dialog boxes are suppressed.

If the file was saved successfully, then Errors will have the value 0; otherwise, it will contain a bitwise OR of the error codes that were generated in saving the document. The masks to check against are the values of the enumerator swFileSaveError_e.
