---
title: "ModelDoc2::InsertSheetMetalHem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSheetMetalHem.htm"
---

# ModelDoc2::InsertSheetMetalHem

This method is obsolete and has been superseded by [FeatureManager::InsertSheetMetalHem](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSheetMetalHem.htm).

Description

This method inserts a sheet metal hem into the current model document.

Syntax (OLE Automation)

ModelDoc2.InsertSheetMetalHem ( type, position, reverse, dLength, dGap, dAngle, dRad, dMiterGap )

| Input: | (long) type | Type as defined in swHemTypes_e |
| --- | --- | --- |
| Input: | (long) position | Position as defined in swHemPositionTypes_e |
| Input: | (VARIANT_BOOL) reverse | TRUE reverses the direction, FALSE does not |
| Input: | (double) dLength | Hem length; valid only for open or closed hems |
| Input: | (double) dGap | Gap distance; valid only for open hems |
| Input: | (double) dAngle | Hem angle; valid only for tear-drop or rolled hems |
| Input: | (double) dRad | Hem radius; valid only for tear-drop or rolled hems |
| Input: | (double) dMiterGap | Hem miter gap |

Syntax (COM)

status = ModelDoc2->InsertSheetMetalHem ( type, position, reverse, dLength, dGap, dAngle, dRad, dMiterGap )

| Input: | (long) type | Type as defined in swHemTypes_e |
| --- | --- | --- |
| Input: | (long) position | Position as defined in swHemPositionTypes_e |
| Input: | (VARIANT_BOOL) reverse | TRUE reverses the direction, FALSE does not |
| Input: | (double) dLength | Hem length; valid only for open or closed hems |
| Input: | (double) dGap | Gap distance; valid only for open hems |
| Input: | (double) dAngle | Hem angle; valid only for tear-drop or rolled hems |
| Input: | (double) dRad | Hem radius; valid only for tear-drop or rolled hems |
| Input: | (double) dMiterGap | Hem miter gap |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
