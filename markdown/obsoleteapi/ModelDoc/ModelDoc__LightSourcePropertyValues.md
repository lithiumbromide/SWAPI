---
title: "ModelDoc::LightSourcePropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__LightSourcePropertyValues.htm"
---

# ModelDoc::LightSourcePropertyValues

This property is obsolete and has been superseded by [ModelDoc2::LightSourcePropertyValues](sldworksAPI.chm::/ModelDoc2/ModelDoc2__LightSourcePropertyValues.htm).

Description

This property gets and sets the light source property values. See also ModelDoc::SetLightSourcePropertyValuesVB, which passes indivudual arguments.

Syntax (OLE Automation)

props = ModelDoc.LightSourcePropertyValues( long ) (VB Get property)

ModelDoc.LightSourcePropertyValues( long ) = props (VB Set property)

props = ModelDoc.GetLightSourcePropertyValues ( id, ) (C++ Get property)

ModelDoc.SetLightSourcePropertyValues ( id, props ) (C++ Set property)

| Input: | (long)id | Light source ID |
| --- | --- | --- |
| Property: | (VARIANT) props | VARIANT of type SafeArray of 19 doubles containing the light source properties |

Syntax (Com)

status = ModelDoc->get_ILightSourcePropertyValues( id, props)

status = ModelDoc->put_ILightSourcePropertyValues ( id, props )

| Input: | (long)id | Light source ID |
| --- | --- | --- |
| Property: | (double*) props | Pointer to an array of 19 doubles containing the light source properties |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use ModelDoc::GetLightSourceCount.

The return values for this method is the following array of 19 doubles:

[ type, Intensity, Color[3], Position[3], Direction[3], coneAngle, falloff[3], Ambient, Specular, isDisabled, SpotExponent ]

where:

- type = is an integer packed into a double that represents the Light Source Type where valid types are taken from openGL Definitions (LIGHT_EYE, LIGHT_AMBIENT, LIGHT_SPOT, LIGHT_POINT, LIGHT_DISTANT)
- Intensity = light source intensity (diffuseness) where values range from 0 to 1.
- Color[3] = light source color in the form of an array of 3 doubles (R, G, B) where values range from 0 to 1.
- Position[3] = light source position for spot lights in the form of an array of 3 doubles (X, Y, Z) in model space.
- Direction[3] = light source direction in the form of an array of 3 doubles (i, j, k)
- coneAngle = light source cone half angle in degrees where valid values are from 0 to 90 and 180.
- falloff[3] = light source falloff in the form of an array of 3 doubles (Kc, Kl, Kq). These values will result in changes in light intensity as the distance between the light position and the vertex change. The result is driven by the following equation:

[ 1 / (Kc + D*Kl + D*D*Kq ) ]

where

- Ambient = light source ambient Intensity
- Specular = light source specular Intensity
- isDisabled = is an integer packed into a double. TRUE means that the light is disabled and FALSE means the light is NOT disabled.
- SpotExponent = the spot exponent
