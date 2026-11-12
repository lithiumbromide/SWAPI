---
title: "ExtrudeFeatureData::GetVertex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetVertex.htm"
---

# ExtrudeFeatureData::GetVertex

This method is obsolete and has been superseded by [ExtrudeFeatureData2::GetVertex](../ExtrudeFeatureData2/ExtrudeFeatureData2__GetVertex.htm).

Description

This method gets the extrusion feature end condition vertex in forward or reverse direction.

Syntax (OLE Automation)

vertex = ExtrudeFeatureData.GetVertex ( forward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (LPDISPATCH) vertex | Dispatch pointer to the end condition vertex (or NULL if the operation fails) |

Syntax (COM)

status = ExtrudeFeatureData->IGetVertex ( forward, &vertex )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (LPVERTEX) vertex | pointer to the end condition vertex (or NULL if the operation fails) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use [ExtrudeFeatureData::AccessSelections](ExtrudeFeatureData__AccessSelections.htm) before calling this method.
