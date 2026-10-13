---
title: "PartDoc::SetMaterialPropertyName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__SetMaterialPropertyName.htm"
---

# PartDoc::SetMaterialPropertyName

This method is obsolete and has been superseded by [PartDoc::SetMaterialPropertyName2](sldworksAPI.chm::/PartDoc/PartDoc__SetMaterialPropertyName2.htm).

Description

This method sets the name of the material property.

Syntax (OLE Automation)

void = PartDoc.SetMaterialPropertyName ( database, name)

| Input: | (BSTR) database | Name of the material database (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) name | Name of the material |

Syntax (COM)

status = PartDoc->SetMaterialPropertyName ( database, name)

| Input: | (BSTR) database | Name of the material database (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) name | Name of the material |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only supports parts.

If the database argument is empty, then the default sldmaterials is used. Otherwise, specify the material database filename and the .sldmat filename extension. For example:

```vb
PartDoc.SetMaterialPropertyName "solidworks materials.sldmat", "Alloy Steel"
```

- or -

```vb
PartDoc.SetMaterialPropertyName "c:/Program Files/SolidWorks/lang/english/sldmaterials/solidworks materials.sldmat", "Alloy Steel"
```
