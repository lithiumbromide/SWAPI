---
title: "ModelDoc::SetDirectionLightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetDirectionLightProperties.htm"
---

# ModelDoc::SetDirectionLightProperties

This method is obsolete and has been superseded by [ModelDoc2::SetDirectionLightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetDirectionLightProperties.htm).

Description

This method sets direction light properties.

Syntax (OLE Automation)

retval = ModelDoc.SetDirectionLightProperties ( name, ambient, diffuse, specular, color, enabled, fixed, xDir, yDir, zDir )

| Input: | (BSTR)name | Light name to modify |
| --- | --- | --- |
| Input: | (double)ambient | Light source ambient value |
| Input: | (double)diffuse | Light source diffuse value |
| Input: | (double)specular | Light source specular value |
| Input: | (long)color | COLORREF color value |
| Input: | (BOOL)enabled | TRUE if the light should be enabled |
| Input: | (BOOL)fixed | TRUE if the light should be fixed |
| Input: | (double)xDir | x component of the light direction vector |
| Input: | (double)yDir | y component of the light direction vector |
| Input: | (double)zDir | z component of the light direction vector |
| Return: | (BOOL) retval | TRUE if light properties were changed successfully |

Syntax (COM)

status = ModelDoc->SetDirectionLightProperties (name, ambient, diffuse, specular, color, enabled, fixed, xDir, yDir, zDir, &retval )

| Input: | (BSTR)name | Light name to be modified |
| --- | --- | --- |
| Input: | (double)ambient | Light source ambient value |
| Input: | (double)diffuse | Light source diffuse value |
| Input: | (double)specular | Light source specular value |
| Input: | (long)color | COLORREF color value |
| Input: | (VARIANT_BOOL)enabled | TRUE if the light should be enabled |
| Input: | (VARIANT_BOOL)fixed | TRUE if the light should be fixed |
| Input: | (double)xDir | x component of the light direction vector |
| Input: | (double)yDir | y component of the light direction vector |
| Input: | (double)zDir | z component of the light direction vector |
| Output: | (VARIANT_BOOL) retval | TRUE if light properties were changed successfully |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks
