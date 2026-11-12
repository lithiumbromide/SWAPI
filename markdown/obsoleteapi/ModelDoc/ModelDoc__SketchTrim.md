---
title: "ModelDoc::SketchTrim"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SketchTrim.htm"
---

# ModelDoc::SketchTrim

This method is obsolete and has been superseded by [ModelDoc2::SketchTrim](../ModelDoc2/ModelDoc2__SketchTrim.htm).

Description

This method trims or extends the selected sketch entity .

Syntax (OLE Automation)

void ModelDoc.SketchTrim ( op, selEnd, x, y)

| Input: | (long) op | Operation to perform: 1= Trim 2 = Extend |
| --- | --- | --- |
| Input: | (long) selEnd | Not used |
| Input: | (double) x | X pick location |
| Input: | (double) y | Y pick location |

Syntax (COM)

status = ModelDoc->SketchTrim ( op, selEnd, x, y )

| Input: | (long) op | Operation to perform: 1= Trim 2 = Extend |
| --- | --- | --- |
| Input: | (long) selEnd | Not used |
| Input: | (double) x | X pick location |
| Input: | (double) y | Y pick location |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
