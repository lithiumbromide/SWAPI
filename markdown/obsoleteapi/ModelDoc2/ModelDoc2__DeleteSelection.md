---
title: "ModelDoc2::DeleteSelection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__DeleteSelection.htm"
---

# ModelDoc2::DeleteSelection

This method is obsolete and has been superseded by [ModelDocExtension::DeleteSelection](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__DeleteSelection2.htm).

Description

This method deletes the selected items without prompting the user for confirmation.

Syntax (OLE Automation)

retval = ModelDoc2.DeleteSelection ( confirmFlag)

| Input: | (BOOL) confirmFlag | TRUE if you want a confirmation dialog to appear, FALSE otherwise |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the item is deleted, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->DeleteSelection ( confirmFlag, &retval )

| Input: | (VARIANT_BOOL) confirmFlag | TRUE if you want a confirmation dialog to appear, FALSE otherwise |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the item is deleted, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
