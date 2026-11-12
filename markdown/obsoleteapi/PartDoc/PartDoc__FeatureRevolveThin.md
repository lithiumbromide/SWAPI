---
title: "PartDoc::FeatureRevolveThin"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__FeatureRevolveThin.htm"
---

# PartDoc::FeatureRevolveThin

This method is obsolete and has been superseded by [FeatureManager::FeatureRevolveThin](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureRevolveThin.htm).

Description

This method creates a feature by revolving a profile about an axis. A constant thickness is given to the profile when revolving. The result is then added to the existing work piece.

Syntax (OLE Automation)

(void) PartDoc.FeatureRevolveThin ( angle, reverseDir, angle2, revType, thickness1, thickness2, thinType )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of feature revolution |
| Input: | (double) thickness1 | Wall thickness 1 (thinType = 2 uses (thickness1 ) /2 for each direction) |
| Input: | (double) thickness2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (long) thinType | Thin feature type: 0 = One direction 1 = One direction reverse 2 = Midplane 3 = Two direction |

Syntax (COM)

status = PartDoc->FeatureRevolveThin ( angle, reverseDir, angle2 revType, thickness1, thickness2, thinType )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Angle is positive or negative (TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (double) thickness1 | Wall thickness 1 (thinType = 2 uses (thickness1 ) /2 for each direction) |
| Input: | (double) thickness2 | Wall thickness 2 (only used when thinType = 3) |
| Input: | (long) thinType | Thin feature Type: 0 = One direction 1 = One direction reverse 2 = Midplane 3 = Two direction |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The revType argument can be one of the following values:

- 0 = One-direction revolution.
- 1 = Midplane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to revolve is (angle/2 ) on either side of the sketch. The reverseDir argument has no affect.
- 2 = Two-direction revolution. For this type of revolve, the angle is the angle to revolve in Direction1 and angle2 is the angle to be revolved in Direction2.
