---
title: "ModelDoc::InsertBendTableNew"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertBendTableNew.htm"
---

# ModelDoc::InsertBendTableNew

This method is obsolete and has been superseded by [ModelDoc2::InsertBendTableNew](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertBendTableNew.htm).

Description

This method inserts a new bend table into the model document.

Syntax (OLE Automation)

ok = ModelDoc.InsertBendTableNew ( filename, units, type )

| Input: | (BSTR) filename | Filename of this new bend table |
| --- | --- | --- |
| Input: | (BSTR) units | Value for units to use for this operation. |
| Input: | (BSTR) type | Value for table type |
| Return: | (BOOL) ok | TRUE if the new table is successfully inserted, FALSE otherwise |

Syntax (COM)

status = ModelDoc->InsertBendTableNew ( filename, units, type, &ok )

| Input: | (BSTR) filename | Filename of this new bend table |
| --- | --- | --- |
| Input: | (BSTR) units | Value for units to use for this operation |
| Input: | (BSTR) type | Value for table type |
| Output: | (VARIANT_BOOL) ok | TRUE if the new table is successfully inserted, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use these values for:

units: "Millimeters", "Centimeters", "Meters","Inches", or "Feet"

type: "Bend Allowance" or "Bend Deduction"
