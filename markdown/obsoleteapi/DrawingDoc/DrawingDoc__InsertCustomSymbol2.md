---
title: "DrawingDoc::InsertCustomSymbol2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertCustomSymbol2.htm"
---

# DrawingDoc::InsertCustomSymbol2

This method is obsolete and has been superseded by [BlockDefinition::InsertInstance](../BlockDefinition/BlockDefinition__InsertInstance.htm) or [DrawingDoc::InsertBlock](DrawingDoc__InsertBlock.htm).

Description

This method inserts a new custom symbol at the selected location without adding the custom symbol to the selection list when the command is finished.

Syntax (OLE Automation)

retval = DrawingDoc.InsertCustomSymbol2 ( fileName )

| Input: | (BSTR) fileName | File name of the custom symbol |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to the newly created custom symbol |

Syntax (COM)

status = DrawingDoc->IInsertCustomSymbol2 ( fileName, &retval )

| Input: | (BSTR) fileName | Filename of the custom symbol |
| --- | --- | --- |
| Output: | (LPCUSTOMSYMBOL) retval | Pointer to the newly created custom symbol |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method depends on something being selected before it is called. If nothing is selected, SolidWorks takes no action and returns NULL.
