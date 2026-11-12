---
title: "ModelDoc::MaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__MaterialPropertyValues.htm"
---

# ModelDoc::MaterialPropertyValues

This property is obsolete and has been superseded by [ModelDoc2::MaterialPropertyValues](sldworksAPI.chm::/ModelDoc2/ModelDoc2__MaterialPropertyValues.htm).

Description

This method gets or sets a material's properties.

Syntax (OLE Automation)

MaterialPropertyValues = ModelDoc.MaterialPropertyValues (VB Get property)

ModelDoc.MaterialPropertyValues = MaterialPropertyValues (VB Set property)

MaterialPropertyValues = ModelDoc.GetMaterialPropertyValues ( ) (C++ Get property)

ModelDoc.SetMaterialPropertyValues ( MaterialPropertyValues ) (C++ Set property)

| Property: | (VARIANT) MaterialPropertyValues | VARIANT of type SafeArray of doubles, describing the material's values |
| --- | --- | --- |

Syntax (Com)

status = ModelDoc->get_IMaterialPropertyValues( MaterialPropertyValues )

status = ModelDoc.put_IMaterialPropertyValues ( MaterialPropertyValues )

| Property: | (double*) MaterialPropertyValues | Array of doubles describing the material's values |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The format of the parameters or return values is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

All elements must be in the range 0 to 1.
