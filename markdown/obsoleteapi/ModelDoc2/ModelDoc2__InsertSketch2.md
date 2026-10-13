---
title: "ModelDoc2::InsertSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__InsertSketch2.htm"
---

# ModelDoc2::InsertSketch2

This method is obsolete and has been superseded by [SketchManager::InsertSketch](sldworksAPI.chm::/SketchManager/SketchManager__InsertSketch.htm).

Description

This method inserts a new sketch in the current part or assembly document.

Syntax (OLE Automation)

void ModelDoc2.InsertSketch2 ( updateEditRebuild )

| Input: | (VARIANT BOOL )updateEditRebuild | TRUE to rebuild the part with any changes made to the sketch and exit sketch mode, FALSE to not |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->InsertSketch2 ( updateEditRebuild )

| Input: | (VARIANT_BOOL) updateEditRebuild | TRUE to rebuild the part with any changes made to the sketch and exit sketch mode, FALSE to not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method does not support drawing documents; NULL is returned if used with a drawing document.
