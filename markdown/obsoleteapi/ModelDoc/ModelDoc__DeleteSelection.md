---
title: "ModelDoc::DeleteSelection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__DeleteSelection.htm"
---

# ModelDoc::DeleteSelection

This method is obsolete and has been superseded by [ModelDoc2::DeleteSelection](../ModelDoc2/ModelDoc2__DeleteSelection.htm).

Description

This method deletes the selected items without prompting for user confirmation.

Syntax (OLE Automation)

retval = ModelDoc.DeleteSelection ( confirmFlag)

| Input: | (BOOL) confirmFlag | TRUE if you want a confirmation dialog to appear, FALSE if not |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the item was deleted successfully, FALSE if not |

Syntax (COM)

status = ModelDoc->DeleteSelection ( confirmFlag, &retval )

| Input: | (VARIANT_BOOL) confirmFlag | TRUE if you want a confirmation dialog to appear, FALSE if not |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the item was deleted successfully, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
