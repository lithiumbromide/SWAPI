---
title: "ExtrudeFeatureData::SetEndCondition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__SetEndCondition.htm"
---

# ExtrudeFeatureData::SetEndCondition

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetEndCondition](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__SetEndCondition.htm).

Description

This method sets the end condition type of the extrusion feature for forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData.SetEndCondition ( forward, endCondition )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (int) endCondition | End condition type as defined in swEndConditions_e |

Syntax (COM)

status = ExtrudeFeatureData->SetEndCondition ( forward, endCondition )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (int) endCondition | End condition type as defined in swEndConditions_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
