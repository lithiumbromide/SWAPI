---
title: "PartDoc::FeatureRevolve"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__FeatureRevolve.htm"
---

# PartDoc::FeatureRevolve

This method is obsolete and has been superseded by [FeatureManager::FeatureRevolve](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureRevolve.htm).

Description

This method creates a revolved feature. This feature is either a base feature or a subsequent boss feature.

Syntax (OLE Automation)

void PartDoc.FeatureRevolve ( angle, reverseDir, angle2, revType)

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Positive or negative angle (TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |

Syntax (COM)

status = PartDoc->FeatureRevolve ( angle, reverseDir, angle2, revType )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Positive or negative angle (TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The revType argument can be one of the following values:

- 0 = One-direction revolution.
- 1 = Midplane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to revolve is (angle/2 ) on either side of the sketch. The reverseDir argument has no affect.
- 2 = Two-direction revolution. For this type of revolve, the angle is the angle to revolve in Direction1 and angle2 is the angle to be revolved in Direction2.
