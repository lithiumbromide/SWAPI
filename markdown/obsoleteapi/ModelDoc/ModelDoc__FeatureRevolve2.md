---
title: "ModelDoc::FeatureRevolve2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__FeatureRevolve2.htm"
---

# ModelDoc::FeatureRevolve2

This method is obsolete and has been superseded by [ModelDoc2::FeatureRevolve2](../ModelDoc2/ModelDoc2__FeatureRevolve2.htm).

Description

This method creates a revolved feature. This feature is either a base feature or a subsequent boss feature.

Syntax (OLE Automation)

retval = ModelDoc.FeatureRevolve2 ( angle, reverseDir, angle2, revType, Options)

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (BOOL) reverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (long) Options | Additional control |
| Return: | (long) retval | 0 for no error |

Syntax (COM)

status = ModelDoc->FeatureRevolve2( angle, reverseDir, angle2, revType, Options, &retval )

| Input: | (double) angle | Angle of revolution in radians |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) reverseDir | Angle is positive or negative ( TRUE or FALSE) |
| Input: | (double) angle2 | Angle of revolution in radians |
| Input: | (long) revType | Type of revolution |
| Input: | (long) Options | Additional control |
| Output: | (long) retval | 0 for no error |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The Options argument allows additional control of the feature creation. Supported values are listed in swoptions.h.
