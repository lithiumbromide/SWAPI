---
title: "ModelDoc2::Insert3DSketch2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__Insert3DSketch2.htm"
---

# ModelDoc2::Insert3DSketch2

This method is obsolete and has been superseded by [SketchManager::Insert3DSketch](sldworksAPI.chm::/SketchManager/SketchManager__Insert3DSketch.htm).

Description

This method inserts a new 3D sketch in a model or closes the active sketch.

Syntax (OLE Automation)

ModelDoc2.Insert3DSketch2 (updateEditRebuild )

| Input: | (VARIANT BOOL )updateEditRebuild | TRUE if you want to edit and rebuild, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc2->Insert3DSketch2 (updateEditRebuild )

| Input: | (VARIANT_BOOL) status | TRUE if you want to edit and rebuild, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
