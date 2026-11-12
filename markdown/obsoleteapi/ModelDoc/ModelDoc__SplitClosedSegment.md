---
title: "ModelDoc::SplitClosedSegment"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SplitClosedSegment.htm"
---

# ModelDoc::SplitClosedSegment

This method is obsolete and has been superseded by [ModelDoc2::SplitClosedSegment](../ModelDoc2/ModelDoc2__SplitClosedSegment.htm).

Description

This method splits the selected sketch segment into two sketch segments.

Syntax (OLE Automation)

void ModelDoc.SplitClosedSegment ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | X value of first point |
| --- | --- | --- |
| Input: | (double) y1 | Y value of first point |
| Input: | (double) z1 | Z value of first point |
| Input: | (double) x2 | X value of second point |
| Input: | (double) y2 | Y value of second point |
| Input: | (double) z2 | Z value of second point |

Syntax (COM)

status = ModelDoc->SplitClosedSegment ( x1, y1, z1, x2, y2, z2 )

| Input: | (double) x1 | X value of first point |
| --- | --- | --- |
| Input: | (double) y1 | Y value of first point |
| Input: | (double) z1 | Z value of first point |
| Input: | (double) x2 | X value of second point |
| Input: | (double) y2 | Y value of second point |
| Input: | (double) z2 | Z value of second point |
| Return: | (HRESULT )status | S_OK if successful |

Remarks

The selected sketch segment must be a closed entity; for example, the start point and end point must be the same. To split a closed sketch segment, for example a complete circle, into two pieces, you must specify two points (x1, y1, z1) and (x2, y2, z2).
