---
title: "ModelDoc::SplitOpenSegment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SplitOpenSegment.htm"
---

# ModelDoc::SplitOpenSegment

This method is obsolete and has been superseded by [ModelDoc2::SplitOpenSegment](../ModelDoc2/ModelDoc2__SplitOpenSegment.htm).

Description

This method splits the selected sketch segment into two sketch segments.

Syntax (OLE Automation)

retval = ModelDoc.SplitOpenSegment ( x1, y1, z1 )

| Input: | (double) x | X value of the point, which splits the sketch segment in two |
| --- | --- | --- |
| Input: | (double) y | Y value of the point, which splits the sketch segment in two |
| Input: | (double) z | Y value of the point, which splits the sketch segment in two |

Syntax (COM)

status = ModelDoc->SplitOpenSegment ( x1, y1, z1 )

| Input: | (double) x | X value of the point, which will split the sketch segment in two |
| --- | --- | --- |
| Input: | (double) y | Y value of the point, which will split the sketch segment in two |
| Input: | (double) z | Y value of the point, which will split the sketch segment in two |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selected sketch segment must be an open entity; for example, the start point and end point cannot be the same.
