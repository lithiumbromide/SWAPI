---
title: "ModelDoc2::SaveAs4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SaveAs4.htm"
---

# ModelDoc2::SaveAs4

This method is obsolete and has been superseded by [ModelDocExtension::SaveAs](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__SaveAs.htm).

Description

This method saves the document under a different name.

Syntax (OLE Automation)

retval = ModelDoc2.SaveAs4 ( Name, Version, Options, &Errors, &Warnings )

| Input: | (BSTR) Name | New name of the document' the file extension indicates any conversion that should be performed (for example, Part1.igs to save to IGES) |
| --- | --- | --- |
| Input: | (long) Version | Format in which to save this document as defined in swSaveAsVersion_e |
| Input: | (long) Options | Option indicating how to save the document as defined in swSaveAsOptions_e |
| Output: | (long) Errors | Errors that caused the save to fail as defined in swFileSaveError_e |
| Output: | (long) Warnings | Warnings or extra information generated during the save operation as defined in swFileSaveWarning_e |
| Output: | (BOOL) retval | TRUE if the save is successful, FALSE if not |

Syntax (COM)

status = ModelDoc2->SaveAs4 ( Name, Version, Options, &Errors, &Warnings, &retval )

| Input: | (BSTR) Name | New name of the document; the file extension indicates any conversion that should be performed (for example, Part1.igs to save to IGES) |
| --- | --- | --- |
| Input: | (long) Version | Format in which to save this document as defined in swSaveAsVersion_e |
| Input: | (long) Options | Option indicating how to save the document as defined in swSaveAsOptions_e |
| Output: | (long) Errors | Errors that caused the save to fail as defined in swFileSaveError_e |
| Output: | (long) Warnings | Warnings or extra information generated during the save operation as defined in swFileSaveWarning_e |
| Output: | (BOOL) retval | TRUE if the save is successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method:

- Overwrites existing files unless they are read-only.
- Results in FileSaveNotify being sent to any application listening.
- Removes any configuration-specific bitmap previews, except the current configuration's.

Saving a document as PDF when the document is open as view-only is not supported.

Do not use ModelDoc2::SaveAs4 to copy assemblies, drawings, or parts with in-context references. Instead, use SldWorks::CopyDocument.

The Name argument refers to the new name for the saved document. The filename extension indicates any conversion that should be performed (for example, "Part1.igs" to save to IGES). If the filename extension does not uniquely indicate how the file should be saved, use the Version argument to determine how to save the file. For example, to save:

- A standard drawing document as a detached drawing, specify swSaveAsDetachedDrawing for Version.
- A detached drawing as a standard drawing, specify swSaveAsStandardDrawing for Version.
- A standard or detached drawing document in the same format, specify swSaveAsCurrentVersion for Version.

You can specify additional Save As options using SldWorks::SetUserPreferenceIntegerValue swUserPreferenceIntegerValue. For example:

```vb
' Save assembly as multibody part and save exterior faces as surface bodies
swApp.SetUserPreferenceIntegerValue swSaveAssemblyAsPartOptions, _
swSaveAsmAsPart_ExteriorFaces
swModelDoc.SaveAs4 "H:\Assem1.SLDPRT", swSaveAsCurrentVersion, _
swSaveAsOptions_Silent, nErrors, nWarnings

- or -

' Save all drawing sheets in active drawing document as an eDrawings file
swApp.SetUserPreferenceIntegerValue swEdrawingsSaveAsSelectionOption, swEdrawingSaveAll
swModelDoc.SaveAs4 "H:\Grid.edrw", swSaveAsCurrentVersion, _
swSaveAsOptions_Silent, nErrors, nWarnings
```

If the file is saved successfully, then the retval is TRUE and the Errors argument is 0. If the save is not successful, then the retval is FALSE and the Errors argument contains a bitwise OR of the error codes that were generated in saving the document. Check the masks against the swFileSaveError_e enumeration. If you do not want SolidWorks to return error information, you can pass in NULL for the Errors argument.

Even if the file is saved successfully, there might be warnings or information that occurs during the save in which you might be interested. The Warnings argument contains a bitwise OR of the warning codes that were generated when saving the document. Check the masks against the swFileSaveWarning_e enumeration. If you do not want warning information returned, you can pass in NULL for the Warnings argument.

Use ModelDoc2::Save3 to save a file using its current name.
