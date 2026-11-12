---
title: "ModelDocExtension::GetPersistReferenceCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetPersistReferenceCount.htm"
---

# ModelDocExtension::GetPersistReferenceCount

This method is obsolete and has been superseded by [ModelDocExtension::GetPersistReferenceCount3](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetPersistReferenceCount3.htm).

Description

This method gets the size of the persistent reference ID assigned to the selected object in this model document.

Syntax (OLE Automation)

*count = ModelDocExtension.GetPersistReferenceCount ( dispObj)

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the selected object |
| --- | --- | --- |
| Output: | (long *) *count | Size of that object's persistent reference ID |

Syntax (COM)

status = ModelDocExtension->GetPersistReferenceCount ( dispObj, &*count)

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the selected object |
| --- | --- | --- |
| Output: | (long *) *count | Size of that object's persistent reference ID |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call this method before calling the COM version ModelDocExtension::GetPersistReference.
