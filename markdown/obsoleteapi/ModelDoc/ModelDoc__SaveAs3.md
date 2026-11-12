---
title: "ModelDoc::SaveAs3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SaveAs3.htm"
---

# ModelDoc::SaveAs3

This method is obsolete and has been superseded by [ModelDoc2::SaveAs3](../ModelDoc2/ModelDoc2__SaveAs3.htm).

Description

This method saves the document with a new name.

Syntax (OLE Automation)

retval = ModelDoc.SaveAs3 ( newName, saveAsVersion, options )

| Input: | (BSTR) newName | New name of the document; the file extension will indicate any conversion that should be performed (for example, Part1.igs to save to IGES) |
| --- | --- | --- |
| Input: | (long) saveAsVersion | See swSaveAsVersion_e for valid options |
| Input: | (long) options | See swSaveAsVersion_e for valid options |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |

Syntax (COM)

status = ModelDoc->SaveAs3 ( newName, saveAsVersion, options, &retval )

| Input: | (BSTR) newName | New name of the document; the file extension will indicate any conversion that should be performed (for example, Part1.igs to save to IGES) |
| --- | --- | --- |
| Input: | (long) saveAsVersion | See swSaveAsVersion_e for valid options |
| Input: | (long) options | See swSaveAsVersion_e for valid options |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The options argument is a bitmask containing various BOOLEANS that affect the outcome of the document saving.

If the file was saved successfully, then retval will have the value 0; otherwise, it will contain a bitwise OR of the error codes that were generated in saving the document. The masks to check against can be found in the swFileSaveError_e enumeration.

This method overwrites existing files on disk unless they are read-only.

This method results in FileSaveAsNotify being sent to any application listening.

To save a file using its current name, see ModelDoc::Save2.
