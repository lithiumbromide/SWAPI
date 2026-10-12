---
title: "ModelDoc::GetDirectionLightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetDirectionLightProperties.htm"
---

# ModelDoc::GetDirectionLightProperties

This method is obsolete and has been superseded by [ModelDoc2::GetDirectionLightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetDirectionLightProperties.htm).

Description

This method gets the direction light properties.

Syntax (OLE Automation)

retval = ModelDoc.GetDirectionLightProperties ( name, &ambient, &diffuse, &specular, &color, &enabled, &fixed, &xDir, &yDir, &zDir )

| Input: | (BSTR) name | Light name |
| --- | --- | --- |
| Output: | (double) ambient | Light source ambient value |
| Output: | (double) diffuse | Light source diffuse value |
| Output: | (double) specular | Light source specular value |
| Output: | (long) color | COLORREF color value |
| Output: | (BOOL) enabled | TRUE if a light is enabled, FALSE if jnot |
| Output: | (BOOL )fixed | TRUE if a light is fixed, FALSE if not |
| Output: | (double) xDir | x component of the light direction vector |
| Output: | (double) yDir | y component of the light direction vector |
| Output: | (double) zDir | z component of the light direction vector |
| Return: | (BOOL) retval | TRUE if light properties determined without a problem, FALSE if not |

Syntax (COM)

status = ModelDoc->GetDirectionLightProperties (name, &ambient, &diffuse, &specular, &color, &enabled, &fixed, &xDir, &yDir, &zDir, &retval )

| Input: | (BSTR) name | Light name |
| --- | --- | --- |
| Output: | (double) ambient | Light source ambient value |
| Output: | (double) diffuse | Light source diffuse value |
| Output: | (double) specular | Light source specular value |
| Output: | (long)c olor | COLORREF color value |
| Output: | (VARIANT_BOOL) enabled | TRUE if a light is enabled, FALSE if not |
| Output: | (VARIANT_BOOL) fixed | TRUE if a light is fixed, FALSE if not |
| Output: | (double) xDir | x component of the light direction vector |
| Output: | (double) yDir | y component of the light direction vector |
| Output: | (double) zDir | z component of the light direction vector |
| Output: | (VARIANT_BOOL) retval | TRUE if light properties determined without a problem, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
