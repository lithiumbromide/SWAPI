---
title: "ModelDoc::InsertSweepRefSurface2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSweepRefSurface2.htm"
---

# ModelDoc::InsertSweepRefSurface2

This method is obsolete and has been superseded by [ModelDoc2::InsertSweepRefSurface2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertSweepRefSurface2.htm).

Description

This method creates a reference surface by sweeping the selected profile along the selected sweep curves. Because you are creating a surface, the sections can be open.

Syntax (OLE Automation)

(void) ModelDoc.InsertSweepRefSurface2 ( propagate, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (Boolean) propagate | If TRUE, then the sweep will propagate to the next edge, FALSE will cause the sweep to occur only on the selected edge NOTE : To propagate to the next edge, the next edge must be tangent to the current edge. |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (Boolean) keepTangency | Follow path |
| Input: | (Boolean) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |

Syntax (COM)

status = ModelDoc->InsertSweepRefSurface2 ( propagate, twistCtrlOption, keepTangency, forceNonRational, startMatchingType, endMatchingType )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the sweep will propagate to the next edge, FALSE will cause the sweep to occur only on the selected edge NOTE : To propagate to the next edge, the next edge must be tangent to the current edge. |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Input: | (short) startMatchingType | Tangency type |
| Input: | (short) endMatchingType | Tangency type |
|  |  |  |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use SelectByMark and AndSelectByMark to select the profile and sweep curves. The mark for the profile selection should be a 1, the mark for the sweep path should be 4. If guide curve selection is provided, the SelectByMark mark should be 2.

The twistCtrlOption may take one of the following values:

- 0 = Follow path
- 1 = Keep constant normal
- 2 = Follow path and first guide curve
- 3 = Follow first and second guide curve

The tangency type arguments may take the following values:

- 0 - none
- 1 - tangent to the normal of the profile
- 2 - tangent to a selected vector
- 3 - tangency to all the adjacent faces sharing an edge with the start profile
- 4 - tangent to some of the selected faces sharing an edge with the start profile (not available at this moment)
