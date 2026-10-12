---
title: "BomTable::Attach2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BOMTable/BomTable__Attach2.htm"
---

# BomTable::Attach2

This method is obsolete and has been superseded by [BomTable::Attach3](sldworksAPI.chm::/BOMTable/BomTable__Attach3.htm).

Description

This method activates the BOM.

Syntax (OLE Automation)

retval = BomTable.Attach2 ()

| Return: | (BOOL) retval | TRUE if it was successfully attached, FALSE if it was not |
| --- | --- | --- |

Syntax (COM)

status = BomTable->Attach2 ( &retval )

| Output: | (VARIANT_BOOL) retval | TRUE if it was successfully attached, FALSE if it was not |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Call this method before you use any of the BomTable methods.
