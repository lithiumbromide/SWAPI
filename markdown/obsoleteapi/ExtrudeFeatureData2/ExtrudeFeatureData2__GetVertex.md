---
title: "ExtrudeFeatureData2::GetVertex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData2/ExtrudeFeatureData2__GetVertex.htm"
---

# ExtrudeFeatureData2::GetVertex

This method is obsolete and has been superseded by [ExtrudeFeatureData2::GetEndConditionReference](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__GetEndConditionReference.htm).

Description

This method gets the extrusion feature end condition vertex in forward or reverse direction.

Syntax (OLE Automation)

vertex = ExtrudeFeatureData.GetVertex ( forward )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (LPDISPATCH) vertex | Dispatch pointer to the end condition vertex object or NULL if the operation fails |

Syntax (COM)

status = ExtrudeFeatureData->IGetVertex ( forward, &vertex)

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (LPVERTEX) vertex | Pointer to the end condition vertex object or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ExtrudeFeatureData2::AccessSelections before calling this method.
