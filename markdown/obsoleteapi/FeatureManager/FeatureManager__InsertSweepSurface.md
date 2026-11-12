---
title: "FeatureManager::InsertSweepSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__InsertSweepSurface.htm"
---

# FeatureManager::InsertSweepSurface

This method is obsolete and has been superseded by [FeatureManager::InsertSweepSurface2](sldworksAPI.chm::/FeatureManager/FeatureManager__InsertSweepSurface2.htm).

Description

This method creates a reference surface by sweeping the selected profile along the selected sweep curves. Because you are creating a surface, the sections can be open.

Syntax (OLE Automation)

(void) FeatureManager.InsertSweepSurface ( propagate, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the sweep propagates to the next edge, FALSE causes the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Start tangency type: 0 = None 1 = Tangent to the normal of the profile 2 = Tangent to a selected vector 3 = Tangency to all the adjacent faces sharing an edge with the start profile 4 = Tangent to some of the selected faces sharing an edge with the start profile (not yet available) |
| Input: | (short) endMatchingType | End tangency type: 0 - None 1 - Tangent to the normal of the profile 2 - Tangent to a selected vector 3 - Tangency to all the adjacent faces sharing an edge with the start profile 4 - Tangent to some of the selected faces sharing an edge with the start profile (not yet available) |
| Input: | (short) alignPath | Available when twistCtrlOption is set to 0 (follow path). Align path type: 0 = None; no correction (default) 2 = Direction vector; a plane, planar face, or line defines the path 3 = All faces; includes neighboring faces |

Syntax (COM)

status = FeatureManager->InsertSweepSurface ( propagate, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL)propagate | If TRUE, then the sweep propagates to the next edge, FALSE causes the sweep to occur only on the selected edge; to propagate to the next edge, the next edge must be tangent to the current edge |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options: 0 = Follow path 1 = Keep constant normal 2 = Follow path and first guide curve 3 = Follow first and second guide curve |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Start tangency type: 0 = None 1 = Tangent to the normal of the profile 2 = Tangent to a selected vector 3 = Tangency to all the adjacent faces sharing an edge with the start profile 4 = Tangent to some of the selected faces sharing an edge with the start profile (not yet available) |
| Input: | (short) endMatchingType | End tangency type: 0 = None 1 = Tangent to the normal of the profile 2 = Tangent to a selected vector 3 = Tangency to all the adjacent faces sharing an edge with the start profile 4 = Tangent to some of the selected faces sharing an edge with the start profile (not yet available) |
| Input: | (short) alignPath | Available when twistCtrlOption is set to 0 (follow path). Align path type: 0 = None; no correction (default) 2 = Direction vector; a plane, planar face, or line defines the path 3 = All faces; includes neighboring faces |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use ModelDocExtension::SelectByID to select the profile and sweep curves with these marks:

- 1 = profile selection
- 4 = sweep path
- 2 = guide curve selection, if provided
