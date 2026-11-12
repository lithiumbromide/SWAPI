---
title: "PartDoc::FeatureRevolveThinCut"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__FeatureRevolveThinCut.htm"
---

# PartDoc::FeatureRevolveThinCut

This method is obsolete and has been superseded by [FeatureManager::FeatureRevolveThinCut](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureRevolveThinCut.htm).

Description

This method creates a feature by revolving a profile about an axis. A constant thickness is given to the profile when revolving. The result is then removed from the existing work piece

Syntax (OLE Automation)

(void) PartDoc.FeatureRevolveThinCut ( angle, reverseDir, angle2, revType, thickness1, thickness2, thinType )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Angle is positive or negative (TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (double) thickness1 | Wall thickness 1 (thinType = 2 uses (thickness1 ) /2 for each direction) |
| Input: | (double) thickness2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (long) thinType | Thin feature type: 0 = One direction 1 = One direction reverse 2 = Midplane 3 = Two direction |

Syntax (COM)

status = PartDoc->FeatureRevolveThinCut ( angle, reverseDir, angle2, revType, thickness1, thickness2, thinType )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Angle is positive or negative (TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (double) thickness1 | Wall thickness 1 (thinType = 2 uses (thickness1 ) /2 for each direction) |
| Input: | (double) thickness2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (long) thinType | Thin feature type: 0 = One direction 1 = One direction reverse 2 = Midplane 3 = Two direction |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Type of revolution:

- 0= one direction
- 1= midPlane
- 2=two direction
