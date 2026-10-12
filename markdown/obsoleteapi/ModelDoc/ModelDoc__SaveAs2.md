---
title: "ModelDoc::SaveAs2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveAs2.htm"
---

# ModelDoc::SaveAs2

This method is now obsolete and has been superseded by [ModelDoc::SaveAs3](ModelDoc__SaveAs3.htm)

Description

This method saves the document with a new name.

Syntax (OLE Automation)

retval = ModelDoc.SaveAs2 ( newName, unused, saveAsCopy, silent )

| Input: | (BSTR) newName | New name of the document; the file extension will indicate any conversion that should be performed for example, Part1.igs to save to IGES) |
| --- | --- | --- |
| Input: | (long) unused | Not used, pass 0 for this argument |
| Input: | (BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name in the active session; documents that reference the document will continue to reference the original file |
| Input: | (BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs displayed |
| Return: | (long) retval | 0 if no errors during save; otherwise, errors occurred |

Syntax (COM)

status = ModelDoc->SaveAs2 ( newName, unused, saveAsCopy, silent, &retval )

| Input: | (BSTR) newName | New name of the document; the file extension will indicate any conversion that should be performed (for example, Part1.igs to save to IGES) |
| --- | --- | --- |
| Input: | (long) unused | Not used; pass 0 for this argument |
| Input: | (VARIANT_BOOL) saveAsCopy | TRUE to save the document to a new filename without replacing the name in the active session; documents that reference the document will continue to reference the original file |
| Input: | (VARIANT_BOOL) silent | TRUE if you want to avoid error and warning dialogs, FALSE if you want the dialogs displayed |
| Output: | (long) retval | 0 if no errors during s; otherwise, errors occurred |
| Return: | (HRESULT)status | S_OK if successful; S_FALSE otherwise |

Remarks

The name of the document must be the filename and the file extension. The file path is optional. If the path is not specified, then the file ise saved in the current working directory.

If the file was saved successfully, then retval will have the value 0;otherwise it will contain a bitwise OR of the error codes that were generated in saving the document. The masks to check against can be found in the swFileSaveError_e enumeration.

This method overwrites existing files on disk unless they are read-only.

This method results in FileSaveAsNotify being sent to any application listening.

To save a file using its current name, see ModelDoc::Save2.
