---
title: "Feature::SetMaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__SetMaterialPropertyValues.htm"
---

# Feature::SetMaterialPropertyValues

This method is obsolete and has been superseded by [Feature::SetMaterialPropertyValues2](sldworksAPI.chm::/Feature/Feature__SetMaterialPropertyValues2.htm).

Description

This method sets the material properties for this feature. The material values include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency and emission. Valid values are from 0 to 1 for all variables.

Syntax (OLE Automation)

retval = Feature.SetMaterialPropertyValues ( MaterialPropertyValues)

| Input: | (VARIANT) MaterialPropertyValues | Property values of the material for this feature |
| --- | --- | --- |
| Return: | (VARIANT_BOOL) retval | TRUE if the material property values were set successfully, FALSE if not |

Syntax (COM)

status = Feature->ISetMaterialPropertyValues ( MaterialPropertyValues, &retval )

| Input: | (double*) MaterialPropertyValues | Property values of the material for this feature |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the material property values were set successfully, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The format of the variant is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

To reset the feature to use the default part material properties, refer to ModelDoc2::SelectedFeatureProperties
