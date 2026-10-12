---
title: "Sheet::GetBomTable"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Sheet/Sheet__GetBomTable.htm"
---

# Sheet::GetBomTable

This method is obsolete because BOM tables are now supported on a per view basis. See [View::GetBomTable](sldworksAPI.chm::/View/View__GetBomTable.htm).

Description

This method returns the BOMTable object on the drawing sheet.

Syntax (OLE Automation)

retval = Sheet.GetBomTable ()

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the BomTable object |
| --- | --- | --- |

Syntax (COM)

status = Sheet->IGetBomTable ( &retval )

| Output: | (LPBOMTABLE) retval | Pointer to the BomTable object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
