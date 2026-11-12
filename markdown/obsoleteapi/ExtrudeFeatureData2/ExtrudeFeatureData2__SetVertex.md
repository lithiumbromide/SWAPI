---
title: "ExtrudeFeatureData2::SetVertex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData2/ExtrudeFeatureData2__SetVertex.htm"
---

# ExtrudeFeatureData2::SetVertex

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetEndConditionReference](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__SetEndConditionReference.htm).

Description

This method sets the extrusion feature end-condition vertex in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData2.SetVertex ( forward, vertex )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (LPDISPATCH) vertex | Dispatch pointer to the end-condition vertex |

Syntax (COM)

status = ExtrudeFeatureData2->ISetVertex ( forward, vertex)

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (LPVERTEX) vertex | Pointer to the end-condition vertex |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ExtrudeFeatureData2::AccessSelections before calling this method.
