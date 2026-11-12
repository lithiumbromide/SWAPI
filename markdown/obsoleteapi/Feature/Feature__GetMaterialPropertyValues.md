---
title: "Feature::GetMaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__GetMaterialPropertyValues.htm"
---

# Feature::GetMaterialPropertyValues

This method is obsolete and has been superseded by [Feature::GetMaterialPropertyValues2](sldworksAPI.chm::/Feature/Feature__GetMaterialPropertyValues2.htm).

Description

This method gets the material properties for this feature. The material values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency and emission. Valid values are from 0 to 1 for all variables.

Syntax (OLE Automation)

retval = Feature.GetMaterialPropertyValues ()

| Return: | (VARIANT) retval | Property values of the material for this feature (see below) |
| --- | --- | --- |

Syntax (COM)

status = Feature->IGetMaterialPropertyValues ( retval )

| Output: | (double*) retval | Array of doubles describing the material values (see below) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method returns NULL if this feature was not explicitly modified from the material property values of the body. If you create a body and change the body color to red, then Feature::GetMaterialPropertyValues returns a NULL array because you did not specifically change the values of the feature.

The format of the return value is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]
