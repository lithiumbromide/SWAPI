---
title: "BomTable::GetColumnCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BOMTable/BomTable__GetColumnCount.htm"
---

# BomTable::GetColumnCount

This method is obsolete and has been superseded by [BomTable::GetTotalColumnCount](sldworksAPI.chm::/BOMTable/BomTable__GetTotalColumnCount.htm).

Description

This method gets the number of columns in the BOM table.

Syntax (OLE Automation)

retval = BomTable.GetColumnCount ()

| Return: | (long) retval | Number of columns in the BOM table |
| --- | --- | --- |

Syntax (COM)

status = BomTable->GetColumnCount ( &retval )

| Output: | (long) retval | Number of columns in the BOM table |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method only returns the visible columns in the BOM table.

Before you use any of the BomTable methods, you must first activate the BOM Table using [BomTable::Attach](BomTable__Attach.htm). After you finish getting BOM data, use BomTable::Detach to deactivate the table.

This method returns 0 if the BOM is obscured, which may occur when debugging a macro. This is a quirk in Microsoft Excel, which is used by SolidWorks for the BOM functionality.
