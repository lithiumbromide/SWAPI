---
title: "Face::GetPatternSeedFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Face/Face__IGetPatternSeedFeature.htm"
---

# Face::GetPatternSeedFeature

This method is obsolete and has been superseded by [Face2::GetPatternSeedFeature](sldworksAPI.chm::/Face2/Face2__GetPatternSeedFeature.htm).

Description

This method gets the seed feature of a pattern face.

Syntax (OLE Automation)

seedFeature = Face.GetPatternSeedFeature ( )

| Output: | (LPDISPATCH) seedFeature | Seed feature of the current face. If the face does not belong to a pattern, this argument is NULL. |
| --- | --- | --- |

Syntax (COM)

status = Face->IGetPatternSeedFeature ( &seedFeature )

| Output: | (LPFEATURE) seedFeature | Seed feature of the current face. If the face does not belong to a pattern, this argument is NULL. |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
