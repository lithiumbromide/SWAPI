---
title: "ModelDoc::SetPointLightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetPointLightProperties.htm"
---

# ModelDoc::SetPointLightProperties

This method is obsolete and has been superseded by [ModelDoc2::SetPointLightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetPointLightProperties.htm).

Description

This method sets point light properties.

Syntax (OLE Automation)

retval = ModelDoc.SetPointLightProperties ( name, ambient, diffuse, specular, color, enabled, fixed, x, y, z )

| Input: | (BSTR) name | Light name to be modified |
| --- | --- | --- |
| Input: | (double) ambient | Light source ambient value |
| Input: | (double) diffuse | Light source diffuse value |
| Input: | (double) specular | Light source specular value |
| Input: | (long) color | COLORREF color value |
| Input: | (BOOL) enabled | TRUE if the light should be enabled |
| Input: | (BOOL) fixed | TRUE if the light should be fixed |
| Input: | (double) x | x location of the point light |
| Input: | (double) y | y location of the point light |
| Input: | (double) z | z location of the point light |
| Return: | (BOOL) retval | TRUE if the light properties where changed successfully |

Syntax (COM)

status = ModelDoc->SetPointLightProperties (name, ambient, diffuse, specular, color, enabled, fixed, x, y, z, &retval )

| Input: | (BSTR) name | Lght name to be modified |
| --- | --- | --- |
| Input: | (double) ambient | Light source ambient value |
| Input: | (double) diffuse | Light source diffuse value |
| Input: | (double) specular | Light source specular value |
| Input: | (long) color | COLORREF color value |
| Input: | (VARIANT_BOOL) enabled | TRUE if the light should be enabled |
| Input: | (VARIANT_BOOL) fixed | TRUE if the light should be fixed |
| Input: | (double) x | x location of the point light |
| Input: | (double) y | y location of the point light |
| Input: | (double) z | z location of the point light |
| Output: | (VARIANT_BOOL) retval | TRUE if the light properties where changed successfully |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
