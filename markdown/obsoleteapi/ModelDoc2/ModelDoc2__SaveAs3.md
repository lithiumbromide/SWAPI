---
title: "ModelDoc2::SaveAs3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SaveAs3.htm"
---

# ModelDoc2::SaveAs3

This method is obsolete and has been superseded by [ModelDoc2::SaveAs4](ModelDoc2__SaveAs4.htm).

Description

This method saves the document under a different name.

Syntax (OLE Automation)

retval = ModelDoc2.SaveAs3 ( newName, saveAsVersion, options )

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Input: | (long) saveAsVersion | Version as defined in swSaveAsVersion_e |
| Input: | (long) options | Option as defined in swSaveAsOptions_e |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |

Syntax (COM)

status = ModelDoc2->SaveAs3 ( newName, saveAsVersion, options, &retval )

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Input: | (long) saveAsVersion | Version as defined in swSaveAsVersion_e |
| Input: | (long) options | Option as defined in swSaveAsOptions_e |
| Output: | (long) retval | 0 if no errors during save; otherwise, errors occurred |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The options argument is a bitmask containing various BOOLEANS that affect the outcome of saving the document.

If the file was saved without errors, retval has a value of 0. Otherwise, it contains a bitwise OR of the error codes that were generated when saving the document. However, not all of the File, Save return codes are fatal errors. It is a bitmask of different conditions that can occur during the operation; some of which are fatal, some are informational or warnings. Check the masks in swFileSaveError_e.

This method:

- Overwrites existing files on disk unless they are read-only.
- Results in FileSaveAsNotify being sent to any application listening.

To save the referenced part files when using this method on an assembly document, you must specify these enumerators for the Options argument:

- swSaveAsOptions_Silent
- swSaveAsOptions_Copy
- swSaveAsOptions_SaveReferenced
