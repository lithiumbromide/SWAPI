---
title: "ModelDoc::InsertWeldSymbol3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertWeldSymbol3.htm"
---

# ModelDoc::InsertWeldSymbol3

This method is obsolete and has been superseded by [ModelDoc2::InsertWeldSymbol3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertWeldSymbol3.htm).

Description

This method inserts a weld symbol in the model.

Syntax (OLE Automation)

retval = ModelDoc.InsertWeldSymbol3 ( )

| Output: | (LPDISPATCH) retval | Pointer to the new weld symbol |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IInsertWeldSymbol3 ( &retval )

| Output: | (LPWELDSYMBOL) retval | Pointer to the new weld symbol |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

First insert the weld symbol into the model, and then manipulate the properties and methods on the weld symbol object.
