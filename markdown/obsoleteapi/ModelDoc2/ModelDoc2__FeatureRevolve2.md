---
title: "ModelDoc2::FeatureRevolve2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureRevolve2.htm"
---

# ModelDoc2::FeatureRevolve2

This method is obsolete and has been superseded by [FeatureManager::FeatureRevolve](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureRevolve.htm).

Description

This method creates a revolved feature. This feature is either a base feature or boss feature.

Syntax (OLE Automation)

retval = ModelDoc2.FeatureRevolve2 ( angle, reverseDir, angle2, revType, Options)

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | TRUE if angle is positive, FALSE if negative |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (long) Options | Additional control as defined in swAutoCloseSketch |
| Return: | (long) retval | 0 for no error, 1 for error |

Syntax (COM)

status = ModelDoc2->FeatureRevolve2( angle, reverseDir, angle2, revType, Options, &retval )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | TRUE if angle is positive, FALSE if negative |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (long) Options | Additional control as defined in swAutoCloseSketch |
| Output: | (long) retval | 0 if no error, 1 if error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The revType argument can be one of the following values:

- 0 = One-direction revolution.
- 1 = MidPlane revolution. For this type of revolve, the angle argument specifies the full revolution. The angle to revolve is (angle/2) on either side of the sketch. The reverseDir argument has no effect.
- 2 = Two-direction revolution. For a two-direction revolve, the angle argument is the angle to revolve in Direction 1 and angle2 is the angle to be revolved in Direction 2.
