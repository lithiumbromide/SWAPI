---
title: "ModelDoc2::FeatureRevolveCut2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__FeatureRevolveCut2.htm"
---

# ModelDoc2::FeatureRevolveCut2

This method is obsolete and has been superseded by [FeatureManager::FeatureRevolveCut.](sldworksAPI.chm::/FeatureManager/FeatureManager__FeatureRevolveCut.htm)

Description

This method creates a revolved feature cut.

Syntax (OLE Automation)

retval = ModelDoc2.FeatureRevolveCut2 ( angle, reverseDir, angle2, revType, Options)

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | TRUE if angle is positive, FALSE if negative |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution: 1 = MidPlane revolution. For this type of revolve, the angle argument specifies the full revolution. The angle to revolve is (angle/2) on either side of the sketch. The reverseDir argument has no effect. 2 = Two-direction revolution. For a two direction revolve, the angle argument is the angle to revolve in Direction1 and the angle2 argument is the angle to revolve in Direction2. |
| Input: | (long) Options | Additional control as defined in swAutoCloseSketch; close the sketch if it is open |
| Return: | (long) retval | 0 if no error, 1 if error |

Syntax (COM)

status = ModelDoc2->FeatureRevolveCut2( angle, reverseDir, angle2, revType, Options, &retval )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | TRUE if angle is positive, FALSE if negative |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution: 1 = MidPlane revolution. For this type of revolve, the angle argument specifies the full revolution. The angle to revolve is (angle/2) on either side of the sketch. The reverseDir argument has no effect. 2 = Two-direction revolution. For a two direction revolve, the angle argument is the angle to revolve in Direction1 and the angle2 argument is the angle to revolve in Direction2. |
| Input: | (long) Options | Additional control as defined in swAutoCloseSketch; close the sketch if it is open |
| Output: | (long) retval | 0 if no error, 1 if error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
