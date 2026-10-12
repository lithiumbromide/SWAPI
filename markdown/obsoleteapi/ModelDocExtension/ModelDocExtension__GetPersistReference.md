---
title: "ModelDocExtension::GetPersistReference"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDocExtension/ModelDocExtension__GetPersistReference.htm"
---

# ModelDocExtension::GetPersistReference

This method is obsolete and has been superseded by [ModelDocExtension::GetPersistReference3](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__GetPersistReference3.htm).

Description

This method gets the persistent reference ID for the specified object in this model document.

Syntax (OLE Automation)

persistId = ModelDocExtension.GetPersistReference ( dispObj)

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the object |
| --- | --- | --- |
| Output: | (VARIANT*) persistId | VARIANT of type SafeArray containing the persistent reference ID assigned to that object |

Syntax (COM)

status = ModelDocExtension->IGetPersistReference ( dispObj, count, &persistId)

| Input: | (LPDISPATCH) dispObj | Dispatch pointer to the object |
| --- | --- | --- |
| Input: | (long) count | Size of persistId assigned to that object (see Remarks ) |
| Output: | (BYTE*) persistId | Byte array containing the persistent reference ID assigned to that object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To get the size of the byte array, call ModelDocExtension::GetPersistReferenceCount before calling this method.

The internal representations of the persistId array may change, possibly from rebuild to rebuild, or more likely, from one release of SolidWorks to the next, but their usage in finding the correct entity will be consistent across rebuilds and SolidWorks releases.

To compare the referenced entities, you could use the Visual Basic Is operator to find out if the entities are the same.
