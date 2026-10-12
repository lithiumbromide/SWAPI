---
title: "ModelDoc2::SaveSilent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SaveSilent.htm"
---

# ModelDoc2::SaveSilent

This method is obsolete and has been superseded by [ModelDoc2::Save2](ModelDoc2__Save2.htm).

Description

This method saves the current document (with the current name). If it is a new document, use ModelDoc2::SaveAsSilent instead. Dialog boxes are suppressed.

Syntax (OLE Automation)

Errors= ModelDoc2.SaveSilent ( )

| Return: | (long) Errors | 0 for no error or a bitwise OR of the errors defined by swFileSaveError_e |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->SaveSilent ( &Errors)

| Output: | (long) Errors | 0 for no error or a bitwise OR of the errors encountered defined by swFileSaveError_e |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is identical to ModelDoc2::Save except that dialog boxes are suppressed.

If the file was saved successfully then Errors have the value 0; otherwise, Errors contains a bitwise OR of the error codes that were generated in saving the document. Check the masks against the values of the enumerator swFileSaveError_e.
