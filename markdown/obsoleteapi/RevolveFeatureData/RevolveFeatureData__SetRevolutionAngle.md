---
title: "RevolveFeatureData::SetRevolutionAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RevolveFeatureData/RevolveFeatureData__SetRevolutionAngle.htm"
---

# RevolveFeatureData::SetRevolutionAngle

This method is obsolete and has been superseded by [RevolveFeatureData2::SetRevolutionAngle](sldworksAPI.chm::/RevolveFeatureData2/RevolveFeatureData2__SetRevolutionAngle.htm).

Description

This method sets the angle of revolution of the feature in forward/reverse direction.

Syntax (OLE Automation)

void RevolveFeatureData.SetRevolutionAngle ( forward, angle)

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (double) angle | Angle of revolution of the feature in radians |

Syntax (COM)

status = RevolveFeatureData.SetRevolutionAngle ( forward, angle)

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (double) angle | Angle of revolution of the feature in radians |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
