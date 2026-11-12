---
title: "ExtrudeFeatureData2::SetFace"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ExtrudeFeatureData2/ExtrudeFeatureData2__SetFace.htm"
---

# ExtrudeFeatureData2::SetFace

This method is obsolete and has been superseded by [ExtrudeFeatureData2::SetEndConditionReference](sldworksAPI.chm::/ExtrudeFeatureData2/ExtrudeFeatureData2__SetEndConditionReference.htm).

Description

This method sets the end condition face for the extrusion feature in forward or reverse direction.

Syntax (OLE Automation)

void ExtrudeFeatureData2.SetFace ( forward, face )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (LPDISPATCH) face | Dispatch pointer to the end condition face |

Syntax (COM)

status = ExtrudeFeatureData2->ISetFace ( forward, face )

| Input: | (VARIANT_BOOL) forward | TRUE for forward feature direction, FALSE for reverse |
| --- | --- | --- |
| Input: | (LPFACE) face | Pointer to the end condition face |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ExtrudeFeatureData2::AccessSelections before calling this method.
