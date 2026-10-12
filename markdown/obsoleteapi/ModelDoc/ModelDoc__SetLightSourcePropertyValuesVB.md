---
title: "ModelDoc::SetLightSourcePropertyValuesVB"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetLightSourcePropertyValuesVB.htm"
---

# ModelDoc::SetLightSourcePropertyValuesVB

This property is obsolete and has been superseded by [ModelDoc2::SetLightSourcePropertyValuesVB](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetLightSourcePropertyValuesVB.htm).

Description

This method sets the light source property values. This method is similar to the ModelDoc::LightSourcePropertyValues property, but this method allows you to pass each argument individually.

Syntax (OLE Automation)

retval = ModelDoc.SetLightSourcePropertyValuesVB ( IdName, lType, diff, rgbColor, dist, dirX, dirY, dirZ, spotDirX, spotDirY, spotDirZ, spotAngle, fallOff0, fallOff1, fallOff2, ambient, specular, spotExponent, disable)

| Input: | (BSTR) IdName | Light source ID name |
| --- | --- | --- |
| Input: | (int) lType | Light source type where valid types are taken from openGL definitions (LIGHT_EYE, LIGHT_AMBIENT, LIGHT_SPOT, LIGHT_POINT, LIGHT_DISTANT) |
| Input: | (double) diff | Light source diffuseness where values range from 0 to 1 |
| Input: | (long) rgbColor | Color value |
| Input: | (double) dist | Distance between the light source position and the vertex |
| Input: | (double) dirX | X unit vector value describing the lights position |
| Input: | (double) dirY | Y unit vector value describing the lights position |
| Input: | (double) dirZ | Z unit vector value describing the lights position |
| Input: | (double) spotDirX | Spot X direction |
| Input: | (double) spotDirY | Spot Y direction |
| Input: | (double) spotDirZ | Spot Z direction |
| Input: | (double) spotAngle | Spot angle |
| Input: | (double) fallOff0 | Light source falloff - constant attenuation |
| Input: | (double) fallOff1 | Light source falloff - linear attenuation |
| Input: | (double) fallOff2 | Light source falloff - quadratic attenuation |
| Input: | (double) ambient | Llight source ambient intensity |
| Input: | (double) specular | Light source specular intensity |
| Input: | (double) spotExponent | Spot exponent |
| Input: | (BOOL) disable | Light source disabled |
| Return: | (BOOL) retval | Return value is for the SetLightSourcePropertyValuesVB implementation and will return TRUE if setting the light source properties was successful and FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetLightSourcePropertyValuesVB ( IdName, lType, diff, rgbColor, dist, dirX, dirY, dirZ, spotDirX, spotDirY, spotDirZ, spotAngle, fallOff0, fallOff1, fallOff2, ambient, specular, spotExponent, disable, &retval )

| Input: | (BSTR) IdName | Lght source id name |
| --- | --- | --- |
| Input: | (int) lType | Light source type where valid types are taken from openGL definitions (LIGHT_EYE, LIGHT_AMBIENT, LIGHT_SPOT, LIGHT_POINT, LIGHT_DISTANT) |
| Input: | (double) diff | Light Source diffuseness where values range from 0 to 1 |
| Input: | (long) rgbColor | Color value |
| Input: | (double) dist | Distance between the light source position and the vertex |
| Input: | (double) dirX | X unit vector value describing the lights position |
| Input: | (double) dirY | Y unit vector value describing the lights position |
| Input: | (double) dirZ | Z unit vector value describing the lights position |
| Input: | (double) spotDirX | Spot X direction |
| Input: | (double) spotDirY | Spot Y direction |
| Input: | (double) spotDirZ | Spot Z direction |
| Input: | (double) spotAngle | Spot angle |
| Input: | (double) fallOff0 | Light source falloff - constant attenuation |
| Input: | (double) fallOff1 | Light source falloff - linear attenuation |
| Input: | (double) fallOff2 | Light source falloff - quadratic attenuation |
| Input: | (double) ambient | Light source ambient intensity |
| Input: | (double) specular | Light source specular intensity |
| Input: | (double) spotExponent | Spot exponent |
| Input: | (VARIANT_BOOL) disable | Light source disabled |
| Output: | (VARIANT_BOOL) retval | Return value is for the SetLightSourcePropertyValuesVB implementation and will return TRUE if setting the light source properties was successful and FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
