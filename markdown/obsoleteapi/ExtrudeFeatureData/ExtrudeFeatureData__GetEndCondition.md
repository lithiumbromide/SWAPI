---
title: "ExtrudeFeatureData::GetEndCondition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetEndCondition.htm"
---

# ExtrudeFeatureData::GetEndCondition

This method is obsolete and has been superseded by [ExtrudeFeatureData2::GetEndCondition](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__GetEndCondition.htm).

Description

This method gets the end condition type of the extrusion feature for forward or reverse direction.

Syntax (OLE Automation)

endCondition = ExtrudeFeatureData.GetEndCondition ( forward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (int) endCondition | End condition type as defined in swEndConditions_e |

Syntax (COM)

status = ExtrudeFeatureData->GetEndCondition ( forward, &endCondition )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (int) endCondition | End condition type as defined in swEndConditions_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
