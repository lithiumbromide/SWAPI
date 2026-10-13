---
title: "ModelDoc::SaveAsSilent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveAsSilent.htm"
---

# ModelDoc::SaveAsSilent

This method is obsolete and has been superseded by [ModelDoc::SaveAs2](ModelDoc__SaveAs2.htm).

Description

This method saves the current document with a new name. Dialog boxes are suppressed.

Syntax (OLE Automation)

Errors = ModelDoc.SaveAsSilent ( newName, saveAsCopy)

| Input: | (BSTR) newName | New name of the document, which can be a name with suffix or a full path |
| --- | --- | --- |
| Input: | (BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name in the active session; documents that reference the document will continue to reference the original file |
| Return: | (long) Errors | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e |

Syntax (COM)

status = ModelDoc->SaveAsSilent ( newName, saveAsCopy, &Errors)

| Input: | (BSTR) newName | New name of the document, which can be a name with suffix or a full path |
| --- | --- | --- |
| Input: | (BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name in the active session; documents that reference the document will continue to reference the original file |
| Output: | (long) Errors | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is identical to ModelDoc::SaveAs except that dialog boxes are suppressed.

If the file was saved successfully then Errors will have the value 0;otherwise it will contain a bitwise OR of the error codes that were generated in saving the document. The masks to check against are the values of the enumerator swFileSaveError_e.

This method overwrites existing files on disk unless they are read-only.
