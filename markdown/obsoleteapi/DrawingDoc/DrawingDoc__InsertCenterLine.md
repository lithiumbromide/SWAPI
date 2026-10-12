---
title: "DrawingDoc::InsertCenterLine"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertCenterLine.htm"
---

# DrawingDoc::InsertCenterLine

This method is obsolete and has been superseded by [DrawingDoc::InsertCenterLine](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertCenterLine2.htm).

Description

This method inserts a center line based on the selected entities.

Syntax (OLE Automation)

retval = DrawingDoc.InsertCenterLine ( )

| Output: | (VARIANT_BOOL) retval | TRUE to insert a center line, FALSE if not |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->InsertCenterLine ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE to insert a center line, FALSE if not |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method works on the entities that are selected when the method runs.
