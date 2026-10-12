---
title: "ModelDoc::GetSaveFlag"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetSaveFlag.htm"
---

# ModelDoc::GetSaveFlag

This method is obsolete and has been superseded by [ModelDoc2::GetSaveFlag](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetSaveFlag.htm).

Description

This method determines whether the document is currently dirty and needs to be saved.

Syntax (OLE Automation)

retval = ModelDoc.GetSaveFlag ( )

| Return: | (BOOL) retval | TRUE if this document needs to be saved, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetSaveFlag ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if this document needs to be saved, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This flag is used by SolidWorks to determine if the Do you wish to save changes dialog should be displayed when the user tries to close the document. Many operations in SolidWorks cause this flag to be set, and ModelDoc::SetSaveFlag can also be used to set this flag.

If you use this method to check the state of an assembly, SolidWorks sets this flag to TRUE for assemblies only when a sub-assembly has been saved. Even if this flag is set to TRUE for a subassembly, SolidWorks does not mark the assembly as dirty until the subassembly is saved.

After the user has saved the file, this flag is reset to FALSE.
