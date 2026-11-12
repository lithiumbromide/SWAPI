---
title: "BlockInstance::GetNext"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockInstance/BlockInstance__GetNext.htm"
---

# BlockInstance::GetNext

This method is obsolete and was not superseded.

Description

This method gets the next block instance in the drawing view.

Syntax (OLE Automation)

retval = BlockInstance.GetNext ( )

| Output: | (LPBLOCKINSTANCE) retval | Pointer to the next block instance |
| --- | --- | --- |

Syntax (COM)

status = BlockInstance->GetNext ( &retval )

| Output: | (LPBLOCKINSTANCE) retval | Pointer to the next block instance |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The sheet sheet must be visible must be visible. See Sheet::SheetFormatVisible.
