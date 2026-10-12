---
title: "ModelDoc::SelectMidPoint"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SelectMidPoint.htm"
---

# ModelDoc::SelectMidPoint

## ModelDoc::SelectMidpoint

This method is obsolete and has been superseded by [ModelDoc2::SelectMidPoint](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SelectMidPoint.htm).

Description

When an edge is selected, this method puts the midpoint (swSelMIDPOINTS) of that edge on the select list and removes the edge from the select list.

Syntax (OLE Automation)

(void) ModelDoc.SelectMidpoint ( )

Syntax (COM)

status = ModelDoc->SelectMidpoint ( )

| Return: | (HRESULT) status | S_OK if successful |
| --- | --- | --- |

Remarks

If the edge whose midpoint is desired is already on the select list and ModelDoc::AndSelect is used to select it again, then ModelDoc::SelectMidpoint leaves both the edge and the point on the select list.
