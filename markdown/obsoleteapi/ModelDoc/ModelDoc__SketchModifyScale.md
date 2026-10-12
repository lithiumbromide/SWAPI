---
title: "ModelDoc::SketchModifyScale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchModifyScale.htm"
---

# ModelDoc::SketchModifyScale

This method is obsolete and has been superseded by [ModelDoc2::SketchModifyScale](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SketchModifyScale.htm).

Description

This method scales the active or selected sketch.

Syntax (OLE Automation)

retval = ModelDoc.SketchModifyScale ( desiredScale )

| Input: | (int) axisFlag | Amount by which to scale sketch |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if successful, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SketchModifyFlip (desiredScale, &retval)

| Input: | (int) axisFlag | Amount by which to scale sketch |
| --- | --- | --- |
| Output: | (BOOL) retval | TRUE if successful, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
