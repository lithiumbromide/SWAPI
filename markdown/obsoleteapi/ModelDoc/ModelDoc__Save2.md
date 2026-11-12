---
title: "ModelDoc::Save2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__Save2.htm"
---

# ModelDoc::Save2

This method is obsolete and has been superseded by [ModelDoc2::Save2](../ModelDoc2/ModelDoc2__Save2.htm).

Description

This method saves the document using its current name.

Syntax (OLE Automation)

retval = ModelDoc.Save2 ( silent )

| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs displayed |
| --- | --- | --- |
| Return: | (long) retval | 0 for no error or a bitwise OR of the errors encountered; see swFileSaveError_e for a list of possible errors and warnings |

Syntax (COM)

status = ModelDoc->Save2 ( silent, &retval )

| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs displayed |
| --- | --- | --- |
| Output: | (long) retval | 0 for no error or a bitwise OR of the errors encountered; see to swFileSaveError_e for a list of possible errors and warnings |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method results in FileSaveNotify being sent to any application listening.

If this is an unsaved document or to save a file with a new name. See ModelDoc::SaveAs2.
