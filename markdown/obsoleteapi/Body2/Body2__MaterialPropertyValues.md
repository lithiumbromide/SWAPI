---
title: "Body2::MaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__MaterialPropertyValues.htm"
---

# Body2::MaterialPropertyValues

This property is obsolete and has been superseded by [Body2::MaterialPropertyValues2](sldworksAPI.chm::/Body2/Body2__MaterialPropertyValues2.htm).

Description

This property gets or sets the material properties for a body other than the base body.

Syntax (OLE Automation)

MaterialPropertyValues = Body2.MaterialPropertyValues (VB Get property)

Body2.MaterialPropertyValues = MaterialPropertyValues (VB Set property)

MaterialPropertyValues = Body2.GetMaterialPropertyValues ( ) (C++ Get property)

Body2.SetMaterialPropertyValues ( MaterialPropertyValues ) (C++ Set property)

| Property: | (VARIANT) MaterialPropertyValues | VARIANT of type SafeArray of doubles (see Remarks ) |
| --- | --- | --- |

Syntax (Com)

status = Body2->get_IMaterialPropertyValues(MaterialPropertyValues)

status = Body2->put_IMaterialPropertyValues (MaterialPropertyValues)

| Property: | (double*) values | Array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The material values include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid settings are from 0 to 1 for all values.

This property is intended to be used on bodies other than the base body and should follow a call to PartDoc::EnumRelatedBodies2. The format of the parameters or return values is an array of 9 doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]
