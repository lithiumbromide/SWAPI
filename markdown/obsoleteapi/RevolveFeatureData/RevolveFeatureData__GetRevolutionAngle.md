---
title: "RevolveFeatureData::GetRevolutionAngle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/RevolveFeatureData/RevolveFeatureData__GetRevolutionAngle.htm"
---

# RevolveFeatureData::GetRevolutionAngle

This method is obsolete and has been superseded by [RevolveFeatureData2::GetRevolutionAngle](sldworksAPI.chm::/RevolveFeatureData2/RevolveFeatureData2__GetRevolutionAngle.htm).

Description

This method gets the revolution angle of the feature in forward or reverse direction.

Syntax (OLE Automation)

angle = RevolveFeatureData.GetRevolutionAngle ( forward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (double) angle | Revolution angle of the feature in radians |

Syntax (COM)

status = RevolveFeatureData->GetRevolutionAngle ( forward, &angle )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (double) angle | Revolution angle of the feature in radians |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
