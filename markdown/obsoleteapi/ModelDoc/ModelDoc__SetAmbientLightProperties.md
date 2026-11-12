---
title: "ModelDoc::SetAmbientLightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetAmbientLightProperties.htm"
---

# ModelDoc::SetAmbientLightProperties

This method is obsolete and has been superseded by [ModelDoc2::SetAmbientLightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetAmbientLightProperties.htm).

Description

This method sets ambient light properties.

Syntax (OLE Automation)

retval = ModelDoc.SetAmbientLightProperties ( name, ambient, diffuse, specular, color, enabled, fixed )

| Input: | (BSTR) name | Light name whose settings will be modified |
| --- | --- | --- |
| Input: | (double) ambient | Llight source ambient value |
| Input: | (double) diffuse | Light source diffuse value |
| Input: | (double) specular | Light source specular value |
| Input: | (long) color | COLORREF color value |
| Input: | (BOOL) enabled | TRUE if the light should be enabled, FALSE otherwise |
| Input: | (BOOL) fixed | TRUE if the light should be fixed, FALSE otherwise |
| Return: | (BOOL) retval | TRUE if light properties changed successfully |

Syntax (COM)

status = ModelDoc->SetAmbientLightProperties ( name, ambient, diffuse, specular, color, enabled, fixed, &retval )

| Input: | (BSTR) name | Light name whose settings will be modified |
| --- | --- | --- |
| Input: | (double) ambient | Light source ambient value |
| Input: | (double) diffuse | Light source diffuse value |
| Input: | (double) specular | Light source specular value |
| Input: | (long)c olor | COLORREF color value |
| Input: | (VARIANT_BOOL) enabled | TRUE if the light should be enabled, FALSE otherwise |
| Input: | (VARIANT_BOOL) fixed | TRUE if the light should be fixed, FALSE otherwise |
| Output: | (VARIANT_BOOL) retval | TRUE if light properties changed successfully |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
