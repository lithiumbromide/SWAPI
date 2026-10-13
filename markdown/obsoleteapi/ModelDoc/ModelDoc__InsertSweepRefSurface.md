---
title: "ModelDoc::InsertSweepRefSurface"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertSweepRefSurface.htm"
---

# ModelDoc::InsertSweepRefSurface

This method is obsolete and has been superseded by [ModelDoc::InsertSweepRefSurface2](ModelDoc__InsertSweepRefSurface2.htm).

Description

This method creates a reference surface by sweeping the selected profile along the selected sweep curves. Because you are creating a surface, the sections can be open.

Syntax (OLE Automation)

void ModelDoc.InsertSweepRefSurface ( propagate, twistCtrlOption, keepTangency, forceNonRational)

| Input: | (BOOL) propagate | If TRUE, then the sweep will propagate to the next edge, FALSE will cause the sweep to occur only on the selected edge NOTE: To propagate to the next edge, the next edge must be tangent to the current edge. |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (BOOL) keepTangency | Follow path |
| Input: | (BOOL) forceNonRational | Keep constant normal |

Syntax (COM)

status = ModelDoc->InsertSweepRefSurface ( propagate, twistCtrlOption, keepTangency, forceNonRational )

| Input: | (VARIANT_BOOL) propagate | If TRUE, then the sweep will propagate to the next edge, FALSE will cause the sweep to occur only on the selected edge NOTE: To propagate to the next edge, the next edge must be tangent to the current edge. |
| --- | --- | --- |
| Input: | (short) twistCtrlOption | Twist control options |
| Input: | (VARIANT_BOOL) keepTangency | Follow path |
| Input: | (VARIANT_BOOL) forceNonRational | Keep constant normal |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use SelectByMark and AndSelectByMark to select the profile and sweep curves. The mark for the profile selection should be a 1; mark for the sweep path should be 4. If guide curve selection is provided, then SelectByMark mark should be 2.

The twistCtrlOption may take one of the following values:

- 0 = Follow path
- 1 = Keep constant normal
- 2 = Follow path and first guide curve
- 3 = Follow first and second guide curve
