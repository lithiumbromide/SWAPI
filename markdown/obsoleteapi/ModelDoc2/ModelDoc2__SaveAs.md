---
title: "ModelDoc2::SaveAs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SaveAs.htm"
---

# ModelDoc2::SaveAs

This method is obsolete and has been superseded by [ModelDoc2::SaveAs2](ModelDoc2__SaveAs2.htm).

Description

This method saves the document with a new name.

Syntax (OLE Automation)

retval = ModelDoc2.SaveAs ( newName)

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE for success, FALSE for failure |

Syntax (COM)

status = ModelDoc2->SaveAs ( newName, &retval )

| Input: | (BSTR) newName | New name of the document; the file extension indicates any conversion that should be performed; for example, Part1.igs to save to IGES |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE for success, FALSE for failure |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method overwrites existing files on disk unless they are read-only.
