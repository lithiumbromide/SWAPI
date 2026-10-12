---
title: "ModelDocExtension::GetObjectByPersistReference2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetObjectByPersistReference2.htm"
---

# ModelDocExtension::GetObjectByPersistReference2

This method is obsolete and has been superseded by [ModelDocExtension::GetObjectByPersistReference3.](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetObjectByPersistReference3.htm)

Description

This method gets the object assigned to the specified persistent reference ID.

NOTE: A persistent reference ID is related to a model. It is portable and can be saved within the model or in other places. Some persistent reference IDs are general to all models and can be instantiated from all models. Your application must handle persistent reference IDs and their relationships among models.

Syntax (OLE Automation)

*dispObj = ModelDocExtension.GetObjectByPersistReference2 ( persistId, *errorCode)

| Input: | (VARIANT) persistId | Object's persistent reference ID (see Remarks ) |
| --- | --- | --- |
| Output: | (long ) *errorCode | Success or error code as defined by swPersistReferencedObjectStates_e (see Remarks ) |
| Output: | (LPDISPATCH ) *dispObj | Dispatch pointer to the object |

Syntax (COM)

status = ModelDocExtension->IGetObjectByPersistReference2 ( count, *persistId, *errorCode, &dispObj)

| Input: | (long) count | Size of persistent reference ID (see Remarks ) |
| --- | --- | --- |
| Input: | (BYTE ) *persistId | Persistent reference ID (see Remarks ) |
| Output: | (long ) *errorCode | Success or error code as defined by swPersistReferencedObjectStates_e (see Remarks ) |
| Output: | (LPDISPATCH ) *dispObj | Dispatch pointer to the object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Before calling this method:

1. If using the COM version of this method, call ModelDocExtension::GetPersistentReferenceCount to determine the size of the persistent reference ID.
2. Call ModelDocExtension::GetPersistReference to get the object's persistent reference ID.

The swPersistReferencedObject_Suppressed and swPersistReferencedObject_Deleted enumerators only apply to references of topological entities.
