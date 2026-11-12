---
title: "DrawingDoc::MakeCustomSymbol2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__MakeCustomSymbol2.htm"
---

# DrawingDoc::MakeCustomSymbol2

This method is obsolete and has been superseded by [DrawingDoc::MakeBlockDefinition](DrawingDoc__MakeBlockDefinition.htm).

Description

This method makes a custom symbol from the selected sketch entities without adding the custom symbol to the selection list.

Syntax (OLE Automation)

retval = DrawingDoc.MakeCustomSymbol2 ( )

| Return: | (LPDISPATCH) retval | Dispatch pointer to the newly created custom symbol |
| --- | --- | --- |

Syntax (COM)

status = DrawingDoc->IMakeCustomSymbol2 ( &retval )

| Output: | (LPCUSTOMSYMBOL) retval | Pointer to the newly created custom symbol |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method depends on something being selected before it is called. If nothing is selected, SolidWorks takes no action and returns NULL.
