---
title: "ModelDoc::GetPointLightProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetPointLightProperties.htm"
---

# ModelDoc::GetPointLightProperties

This method is obsolete and has been superseded by [ModelDoc2::GetPointLightProperties](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetPointLightProperties.htm).

Description

This method gets the point light properties.

Syntax (OLE Automation)

retval = ModelDoc.GetPointLightProperties ( name, &ambient, &diffuse, &specular, &color, &enabled, &fixed, &x, &y, &z )

| Input: | (BSTR) name | Light name |
| --- | --- | --- |
| Output: | (double) ambient | Light source ambient value |
| Output: | (double) diffuse | Light source diffuse value |
| Output: | (double) specular | Light source specular value |
| Output: | (long) color | COLORREF color value |
| Output: | (BOOL) enabled | TRUE if a light is enabled, FALSE if not |
| Output: | (BOOL) fixed | TRUE if a light is fixed, FALSE if not |
| Output: | (double) x | x location of the point light |
| Output: | (double) y | y location of the point light |
| Output: | (double) z | z location of the point light |
| Return: | (BOOL) retval | TRUE if light properties determined without a problem, FALSE if not |

Syntax (COM)

status = ModelDoc->GetPointLightProperties (name, &ambient, &diffuse, &specular, &color, &enabled, &fixed, &x, &y, &z, &retval )

| Input: | (BSTR) name | Light name |
| --- | --- | --- |
| Output: | (double) ambient | Light source ambient value |
| Output: | (double) diffuse | Light source diffuse value |
| Output: | (double) specular | Light source specular value |
| Output: | (long) color | COLORREF color value |
| Output: | (VARIANT_BOOL) enabled | TRUE if a light is enabled, FALSE if not |
| Output: | (VARIANT_BOOL) fixed | TRUE if a light is fixed, FALSE if nto |
| Output: | (double) x | x location of the point light |
| Output: | (double) y | y location of the point light |
| Output: | (double) z | z location of the point light |
| Output: | (VARIANT_BOOL) retval | TRUE if light properties determined without a problem, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
