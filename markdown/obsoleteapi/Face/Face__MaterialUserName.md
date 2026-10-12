---
title: "Face::MaterialUserName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__MaterialUserName.htm"
---

# Face::MaterialUserName

This method is obsolete and has been superseded by [Face2::MaterialUserName](sldworksAPI.chm::/Face2/Face2__MaterialUserName.htm).

Description

This property gets or sets the material name, which is visible to the user.

Syntax (OLE Automation)

name = Face.MaterialUserName (VB Get property)

Face.MaterialUserName = name (VB Set property)

name = Face.GetMaterialUserName ( ) (C++ Get property)

Face.SetMaterialUserName ( name ) (C++ Set property)

| Property: | (BSTR) name | Material user name property on the individual face |
| --- | --- | --- |

Syntax (COM)

status = Face-> get_MaterialUserName( &name )

status = Face-> put_MaterialUserName( name )

| Property: | (BSTR) name | Material user name property on the individual face |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property is unsupported for faces obtained from reference surface bodies.
