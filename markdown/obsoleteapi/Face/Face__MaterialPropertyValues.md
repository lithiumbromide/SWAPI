---
title: "Face::MaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__MaterialPropertyValues.htm"
---

# Face::MaterialPropertyValues

This property is obsolete and has been superseded by [Face2::MaterialPropertyValues](sldworksAPI.chm::/Face2/Face2__MaterialPropertyValues.htm).

Description

This property gets or sets the material properties for a face.

Syntax (OLE Automation)

MaterialPropertyValues = Face.MaterialPropertyValues (VB Get property)

Face.MaterialPropertyValues = MaterialPropertyValues (VB Set property)

MaterialPropertyValues = Face.GetMaterialPropertyValues ( ) (C++ Get property)

Face.SetMaterialPropertyValues ( MaterialPropertyValues ) (C++ Set property)

| Property: | (VARIANT) MaterialPropertyValues | VARIANT of type SafeArray of doubles that describes the material values on this face |
| --- | --- | --- |

Syntax (COM)

status = Face->get_IMaterialPropertyValues( MaterialPropertyValues)

status = Face->put_IMaterialPropertyValues ( MaterialPropertyValues )

| Property: | (double*) MaterialPropertyValues | Array of doubles that describes the material values on this face |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The material values include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency and emission. All values can be from 0 to 1.

This property returns a NULL VARIANT (or an S_FALSE HRESULT for COM implementations) if this face has not been explicitly modified from the material property values of the body. In other words, if you create a body and change the body color to red, then Face::GetMaterialPropertyValues returns a NULL array because you did not specifically change the values of the face.

The format of the parameters or return values is an array of doubles as follows:

```vb
[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]
```

To reset the face to use the default part material properties, use ModelDoc2::SelectedFaceProperties.

This property is unsupported for faces obtained from reference surface bodies.
