---
title: "PartDoc::GetMaterialPropertyName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetMaterialPropertyName.htm"
---

# PartDoc::GetMaterialPropertyName

This method is obsolete and has been superseded by [PartDoc::GetMaterialPropertyName2](sldworksAPI.chm::/PartDoc/PartDoc__GetMaterialPropertyName2.htm).

Description

This method gets the names of the material database and the material.

Syntax (OLE Automation)

retval = PartDoc.GetMaterialPropertyName (*database)

| Output: | (BSTR *) *database | Name of material database |
| --- | --- | --- |
| Output: | (BSTR*) retval | Name of material |

Syntax (COM)

status = PartDoc->GetMaterialPropertyName ( *database, &retval)

| Output: | (BSTR *) *database | Names of material database |
| --- | --- | --- |
| Output: | (BSTR*) retval | Name of material |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If no material was applied to the part, then database and retval are blank.
