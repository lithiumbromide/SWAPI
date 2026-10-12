---
title: "ModelDoc2::Save2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__Save2.htm"
---

# ModelDoc2::Save2

This method is obsolete and has been superseded by [ModelDoc2::Save3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__Save3.htm).

Description

This method saves the document using its current name.

Syntax (OLE Automation)

retval = ModelDoc2.Save2 ( silent )

| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs displayed to the user |
| --- | --- | --- |
| Return: | (long) retval | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e for a list of possible errors and warnings |

Syntax (COM)

status = ModelDoc2->Save2 ( silent, &retval )

| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs displayed to the user |
| --- | --- | --- |
| Output: | (long) retval | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e for a list of possible errors and warnings |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the file was saved successfully, then retval has the value 0; otherwise, it contains a bitwise OR of the error codes that were generated when saving the document. The masks to check against are the values of the enumerator swFileSaveError_e.

This method results in FileSaveNotify being sent to any application listening.

If this is an unsaved document, or saved to a file with a new name, see ModelDoc2::SaveAs.
