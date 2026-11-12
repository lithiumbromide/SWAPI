---
title: "ModelDoc::FeatureRevolveCut2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureRevolveCut2.htm"
---

# ModelDoc::FeatureRevolveCut2

This method is obsolete and has been superseded by [ModelDoc2::FeatureRevolveCut2](../ModelDoc2/ModelDoc2__FeatureRevolveCut2.htm).

Description

This method creates a revolved feature cut. For extruded feature cuts, see ModelDoc::FeatureCut.

Syntax (OLE Automation)

retval = ModelDoc.FeatureRevolveCut2 ( angle, reverseDir, angle2, revType, Options)

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution, where: 1 = MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to be revolved is ( angle /2 ) on either side of the sketch. The reverseDir argument has no affect. 2 = Two direction revolution. For a two direction revolve, the angle is the angle to be revolved in direction 1 and angle2 is the angle to be revolved in direction 2. |
| Input: | (long) Options | Additional control |
| Return: | (long) retval | 0 for no error |

Syntax (COM)

status = ModelDoc->FeatureRevolveCut2( angle, reverseDir, angle2, revType, Options, &retval )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution, where: 1 = MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to be revolved is ( angle /2 ) on either side of the sketch. The reverseDir argument has no affect. 2 = Two direction revolution. For a two direction revolve, the angle is the angle to be revolved in direction 1 and angle2 is the angle to be revolved in direction 2. |
| Input: | (long) Options | Additional control |
| Output: | (long) retval | 0 for no error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The options argument allows additional control of the feature creation. Supported values are listed in swoptions.h.
