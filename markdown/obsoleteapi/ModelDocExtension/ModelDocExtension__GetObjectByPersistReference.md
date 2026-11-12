---
title: "ModelDocExtension::GetObjectByPersistReference"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetObjectByPersistReference.htm"
---

# ModelDocExtension::GetObjectByPersistReference

This method is obsolete and has been superseded by [ModelDocExtension::GetObjectByPersistReference2](ModelDocExtension__GetObjectByPersistReference2.htm).

Description

This method gets the object assigned to the specified persistent reference ID.

NOTE: A persistent reference ID is related to a model. It is portable and can be saved within the model or in other places. Some persistent reference IDs are general to all models and, thus, can be instantiated from all models. Your application must handle persistent reference IDs and their relationships among models.

Syntax (OLE Automation)

*dispObj = ModelDocExtension.GetObjectByPersistReference ( persistId)

| Input: | (VARIANT) persistId | Object's persistent reference ID (see Remarks ) |
| --- | --- | --- |
| Output: | (LPDISPATCH *) *dispObj | Dispatch pointer to the object |

Syntax (COM)

status = ModelDocExtension->IGetObjectByPersistReference ( count, *persistId, &*dispObj)

| Input: | (long) count | Size of the persistent reference ID (see Remarks ) |
| --- | --- | --- |
| Property: | (BYTE *) *persistId | Persistent reference ID (see Remarks ) |
| Output: | (LPDISPATCH *) *dispObj | Dispatch pointer to the object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before calling this method:

1. Call ModelDocExtension::GetPersistReferenceCount to determine the size of the persistent reference ID if using the COM version of this method.
2. Call ModelDocExtension::GetPersistReference to get the object's persistent reference ID.
