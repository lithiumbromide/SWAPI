---
title: "SldWorks::RemoveFileOpenItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__RemoveFileOpenItem.htm"
---

# SldWorks::RemoveFileOpenItem

This method is obsolete and has been superseded by [SldWorks::RemoveFileOpenItem2](sldworksAPI.chm::/SldWorks/SldWorks__RemoveFileOpenItem2.htm).

Description

This method removes a file type from the File Open list that was added using SldWorks::AddFileOpenItem. The parameters passed to this method should match the parameters you used when calling SldWorks::AddFileOpenItem.

Syntax (OLE Automation)

retval = SldWorks.RemoveFileOpenItem ( CallbackFcnAndModule, Description)

| Input: | (BSTR) CallbackFcnAndModule | Name of module and function used in your call to SldWorks::AddFileOpenItem |
| --- | --- | --- |
| Input: | (BSTR) Description | Description used in your call to SldWorks::AddFileOpenItem |
| Return: | (VARIANT_BOOL) retval | TRUE if successfully removed from the File Type list, FALSE otherwise |

Syntax (COM)

status = SldWorks->RemoveFileOpenItem ( CallbackFcnAndModule, Description, &retval )

| Input: | (BSTR) CallbackFcnAndModule | Name of module and function used in your call to SldWorks::AddFileOpenItem |
| --- | --- | --- |
| Input: | (BSTR) Description | Description used in your call to SldWorks::AddFileOpenItem |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully removed from the File Type list, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
