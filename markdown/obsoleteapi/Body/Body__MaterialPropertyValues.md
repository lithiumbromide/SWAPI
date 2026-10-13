---
title: "Body::MaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body/Body__MaterialPropertyValues.htm"
---

# Body::MaterialPropertyValues

This property is obsolete and has been superseded by [Body2::MaterialPropertyValues](../Body2/Body2__MaterialPropertyValues.htm).

Description

This property gets or sets the material properties for a body other than the base body.

Syntax (OLE Automation)

MaterialPropertyValues = Body.MaterialPropertyValues (VB Get property)

Body.MaterialPropertyValues = MaterialPropertyValues (VB Set property)

MaterialPropertyValues = Body.GetMaterialPropertyValues ( ) (C++ Get property)

Body.SetMaterialPropertyValues ( MaterialPropertyValues ) (C++ Set property)

| Property: | (VARIANT) MaterialPropertyValues | VARIANT of type SafeArray of doubles (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Body->get_IMaterialPropertyValues(MaterialPropertyValues)

status = Body->put_IMaterialPropertyValues (MaterialPropertyValues)

| Property: | (double*) values | Array of doubles (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This property is intended to be used on bodies other than the base body and should follow a call to PartDoc::EnumRelatedBodies.

The material values include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid settings are from 0 to 1 for all values. The format of the parameters or return values is an array of 9 doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]
