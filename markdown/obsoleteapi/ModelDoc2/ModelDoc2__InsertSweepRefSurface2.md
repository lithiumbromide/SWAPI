---
title: "ModelDoc2::InsertSweepRefSurface2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSweepRefSurface2.htm"
---

# ModelDoc2::InsertSweepRefSurface2

This method is obsolete and has been superseded by [FeatureManager::InsertSweepSurface](../FeatureManager/FeatureManager__InsertProtrusionSwept2.htm).

Description

This method creates a reference surface by sweeping the selected profile along the selected sweep curves. Because you are creating a surface, the sections can be open.

Syntax (OLE Automation)

(void) ModelDoc2.InsertSweepRefSurface2 ( propagate, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the sweep propagates to the next edge, FALSE causes the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Start tangency type: 0 - none 1 - tangent to the normal of the profile 2 - tangent to a selected vector 3 - tangency to all the adjacent faces sharing an edge with the start profile 4 - tangent to some of the selected faces sharing an edge with the start profile (not yet available) |
| Input: | (short) endMatchingType | End tangency type: 0 - none 1 - tangent to the normal of the profile 2 - tangent to a selected vector 3 - tangency to all the adjacent faces sharing an edge with the start profile 4 - tangent to some of the selected faces sharing an edge with the start profile (not yet available) |

Syntax (COM)

status = ModelDoc2->InsertSweepRefSurface2 ( propagate, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the sweep propagates to the next edge, FALSE causes the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Start tangency type: 0 - none 1 - tangent to the normal of the profile 2 - tangent to a selected vector 3 - tangency to all the adjacent faces sharing an edge with the start profile 4 - tangent to some of the selected faces sharing an edge with the start profile (not yet available) |
| Input: | (short) endMatchingType | End tangency type: 0 - none 1 - tangent to the normal of the profile 2 - tangent to a selected vector 3 - tangency to all the adjacent faces sharing an edge with the start profile 4 - tangent to some of the selected faces sharing an edge with the start profile (not yet available) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves with these marks:

- 1 = profile selection
- 4 = sweep path
- 2 = guide curve selection, if provided
