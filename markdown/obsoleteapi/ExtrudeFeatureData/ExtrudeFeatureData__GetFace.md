---
title: "ExtrudeFeatureData::GetFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData/ExtrudeFeatureData__GetFace.htm"
---

# ExtrudeFeatureData::GetFace

This method is obsolete and has been superseded by [ExtrudeFeatureData2::GetFace](../ExtrudeFeatureData2/ExtrudeFeatureData2__GetFace.htm).

Description

This method gets the end condition face for the extrusion feature in forward or reverse direction.

Syntax (OLE Automation)

face = ExtrudeFeatureData.GetFace ( forward )

| Input: | (BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Return: | (LPDISPATCH) face | Dispatch pointer to the end condition face (or NULL if the operation fails) |

Syntax (COM)

status = ExtrudeFeatureData->IGetFace ( forward, &face )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Output: | (LPFACE) face | Pointer to the end condition face (or NULL if the operation fails) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use [ExtrudeFeatureData::AccessSelections](ExtrudeFeatureData__AccessSelections.htm) before calling this method.
