---
title: "BomTable::GetRowCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BOMTable/BomTable__GetRowCount.htm"
---

# BomTable::GetRowCount

This method is obsolete and has been superseded by [BomTable::GetTotalRowCount](sldworksAPI.chm::/BOMTable/BomTable__GetTotalRowCount.htm).

Description

This method gets the number of rows in the BOM table.

Syntax (OLE Automation)

retval = BomTable.GetRowCount ()

| Return: | (long) retval | Number of rows in the BOM table |
| --- | --- | --- |

Syntax (COM)

status = BomTable->GetRowCount ( &retval )

| Output: | (long) retval | Number of rows in the BOM table |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method only returns the visible rows in the BOM table.

Before you use any of the BomTable methods, activate the BOM Table using [BomTable::Attach](BomTable__Attach.htm). After you finish getting BOM data, use BomTable::Detach to deactivate the table.

This method returns 0 if the BOM is obscured, which may occur when debugging a macro. This is a quirk in Microsoft Excel, which is used by SolidWorks for the BOM functionality.
