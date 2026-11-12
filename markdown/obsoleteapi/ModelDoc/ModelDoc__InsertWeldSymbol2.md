---
title: "ModelDoc::InsertWeldSymbol2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertWeldSymbol2.htm"
---

# ModelDoc::InsertWeldSymbol2

This method is now obsolete and has be superseded by [ModelDoc::InsertWeldSymbol3](ModelDoc__InsertWeldSymbol3.htm)

Description

This method creates a weld symbol located at the last edge selection.

Syntax (OLE Automation)

void ModelDoc.InsertWeldSymbol2 ( dim1, symbol, dim2, symmetric, fieldWeld, showOtherSide, dashOnTop, peripheral, hasProcess, processValue)

| Input: | (BSTR) dim1 | First text value to the left of the symbol |
| --- | --- | --- |
| Input: | (BSTR) symbol | Weld symbol name |
| Input: | (BSTR) dim2 | Text value to the right of the symbol |
| Input: | (BOOL) symmetric | TRUE will put the symbol on both above and below the horizontal line |
| Input: | (BOOL) fieldWeld | TRUE will put a flag for field welding |
| Input: | (BOOL) showOtherSide | Not used; pass 0 |
| Input: | (BOOL) dashOnTop | TRUE will put the dash line on top |
| Input: | (BOOL) peripheral | TRUE will put a peripheral symbol |
| Input: | (BOOL) hasProcess | TRUE will allow you to specify a processValue |
| Input: | (BSTR) processValue | Process value if hasProcess is set to TRUE |

Syntax (COM)

status = ModelDoc->InsertWeldSymbol2 ( dim1, symbol, dim2, symmetric, fieldWeld, showOtherSide, dashOnTop, peripheral, hasProcess, processValue )

| Input: | (BSTR) dim1 | First text value to the left of the symbol |
| --- | --- | --- |
| Input: | (BSTR) symbol | Weld symbol name |
| Input: | (BSTR) dim2 | Text value to the right of the symbol |
| Input: | (VARIANT_BOOL) symmetric | TRUE will put the symbol on both above and below the horizontal line |
| Input: | (VARIANT_BOOL) fieldWeld | TRUE will put a flag for field welding |
| Input: | (VARIANT_BOOL) showOtherSide | Not used, pass 0 |
| Input: | (VARIANT_BOOL) dashOnTop | TRUE will put the dash line on top |
| Input: | (VARIANT_BOOL) peripheral | TRUE will put a peripheral symbol |
| Input: | (VARIANT_BOOL) hasProcess | TRUE will allow you to specify a processValue |
| Input: | (BSTR) processValue | Process value if hasProcess is set to TRUE |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The symbol argument specifies the weld symbol name. A list of names can be found in the gtol.sym file, which is located in the <installation_dir>/lang/english folder of your SolidWorks installation.
