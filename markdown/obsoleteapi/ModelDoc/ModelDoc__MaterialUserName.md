---
title: "ModelDoc::MaterialUserName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__MaterialUserName.htm"
---

# ModelDoc::MaterialUserName

This property is obsolete and has been superseded by [ModelDoc2::MaterialUserName](sldworksAPI.chm::/ModelDoc2/ModelDoc2__MaterialUserName.htm).

Description

This property gets or sets the material name. This name is visible to the user in the PhotoWorks product.

Syntax (OLE Automation)

name = ModelDoc.MaterialUserName (VB Get property)

ModelDoc.MaterialUserName = name (VB Set property)

name = ModelDoc.GetMaterialUserName ( ) (C++ Get property)

ModelDoc.SetMaterialUserName ( name ) (C++ Set property)

| Property: | (BSTR) name | Material's user name property |
| --- | --- | --- |

Syntax (Com)

status = ModelDoc->get_MaterialUserName ( &Name )

status = ModelDoc->put_MaterialUserName ( name )

| Property: | (BSTR) name | Material's user name property |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
