---
title: "ExtrudeFeatureData::SetVertex"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__SetVertex.htm"
---

# ExtrudeFeatureData::SetVertex

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetVertex](../ExtrudeFeatureData2/ExtrudeFeatureData2__SetVertex.htm).

Description

This method sets the extrusion feature end condition vertex in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData.SetVertex ( forward, vertex )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (LPDISPATCH) vertex | Dispatch pointer to the end condition vertex |

Syntax (COM)

status = ExtrudeFeatureData->ISetVertex ( forward, vertex )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (LPVERTEX) vertex | Pointer to the end condition vertex |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ExtrudeFeatureData2::AccessSelections before calling this method.
