---
title: "ModelDoc2::SplitOpenSegment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SplitOpenSegment.htm"
---

# ModelDoc2::SplitOpenSegment

This method is obsolete and has been superseded to [SketchManager::SplitOpenSegment.](sldworksAPI.chm::/SketchManager/SketchManager__SplitOpenSegment.htm)

Description

This method splits the selected sketch segment into two sketch segments.

Syntax (OLE Automation)

retval = ModelDoc2.SplitOpenSegment ( x1, y1, z1 )

| Input: | (double)x | X value of the point that splits the sketch segment in two |
| --- | --- | --- |
| Input: | (double)y | Y value of the point that splits the sketch segment in two |
| Input: | (double)z | Z value of the point that splits the sketch segment in two |

Syntax (COM)

status = ModelDoc2->SplitOpenSegment ( x1, y1, z1 )

| Input: | (double) x | X value of the point that splits the sketch segment in two |
| --- | --- | --- |
| Input: | (double) y | Y value of the point that splits the sketch segment in two |
| Input: | (double) z | Z value of the point that splits the sketch segment in two |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selected sketch segment must be an open entity; for example, the start and end points cannot be the same.
