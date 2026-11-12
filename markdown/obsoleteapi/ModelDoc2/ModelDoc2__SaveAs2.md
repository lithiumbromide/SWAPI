---
title: "ModelDoc2::SaveAs2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SaveAs2.htm"
---

# ModelDoc2::SaveAs2

This method is obsolete and has been superseded by [ModelDoc2::SaveAs3](ModelDoc2__SaveAs3.htm).

Description

This method saves the current document with a different name.

Syntax (OLE Automation)

retval = ModelDoc2.SaveAs2 ( newName, saveAsVersion, saveAsCopy, silent )

| Input: | (BSTR) newName | New name of the document. The file extension indicates any conversion that should be performed for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Input: | (long) saveAsVersion | Version as defined in swSaveAsVersion_e |
| Input: | (VARIANT_BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name in the active session; documents that reference the document continue to reference the original file |
| Input: | (VARIANT_BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs presented to the end-user |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |

Syntax (COM)

status = ModelDoc2->SaveAs2 ( newName, saveAsVersion, saveAsCopy, silent, &retval )

| Input: | (BSTR) newName | New name of the document. The file extension indicates any conversion that should be performed for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Input: | (long) saveAsVersion | Version as defined in swSaveAsVersion_e |
| Input: | (VARIANT_BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name in the active session; documents that reference the document continue to reference the original file |
| Input: | (VARIANT_BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs presented to the end-user |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The name of the document must be the filename and file extension. The file path is optional. If you do not specify the path, then the file is saved in the current working directory.

If the file is saved successfully then retval has a value of 0; otherwise, it contains a bitwise OR of the error codes that were generated in saving the document. You find the masks to check against in swFileSaveError_e.

This method:

- Overwrites existing files on disk unless they are read-only.
- Results in FileSaveAsNotify being sent to any application listening.
