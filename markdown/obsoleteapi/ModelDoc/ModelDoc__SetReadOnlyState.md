---
title: "ModelDoc::SetReadOnlyState"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetReadOnlyState.htm"
---

# ModelDoc::SetReadOnlyState

This method is obsolete and has been superseded by [ModelDoc2::SetReadOnlyState](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetReadOnlyState.htm).

Description

This method sets the read-only mode for a document.

Syntax (OLE Automation)

Success = ModelDoc.SetReadOnlyState ( ReadOnly )

| Input: | (BOOL) ReadOnly | TRUE to set this document to be read-only, FALSE otherwise |
| --- | --- | --- |
| Return: | (BOOL) Success | TRUE if the document was set to the desired state, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetReadOnlyState ( ReadOnly, &Success )

| Input: | (VARIANT_BOOL) ReadOnly | TRUE to set this document to be read-only, FALSE otherwise |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) Success | TRUE if the document was set to the desired state, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If the file is opened as read-write in SolidWorks, specifying read-only will always work, unless it is a new file in which case it has not been saved yet)

If the file is opened as read-only in SolidWorks, then specifying for read-write will only change the internal SolidWorks state, not the access rights on disk, and will only succeed if it would be possible to open this file with write access. For example, if the file is read-only on disk or if another user has it open with write access, then this method will not change the internal state to writeable; instead, it will remain read-only and FALSE will be returned to indicate failure.
