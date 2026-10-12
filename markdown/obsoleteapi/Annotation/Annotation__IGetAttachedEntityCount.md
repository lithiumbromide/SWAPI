---
title: "Annotation::IGetAttachedEntityCount"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__IGetAttachedEntityCount.htm"
---

# Annotation::IGetAttachedEntityCount

This method is obsolete and has been superseded by [Annotation::GetAttachedEntityCount2](Annotation__GetAttachedEntityCount2.htm).

Description

This method gets the number of items associated with this annotation and creates a static list of elements.

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = Annotation->IGetAttachedEntityCount ( &retval )

| Output: | (long) retval | Number of objects attached to this annotation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

You can use the list of elements created by this method with Annotation::IGetAttachedEntities and Annotation::IGetAttachedEntityTypes.

This method supports all annotation types. See Annotation::GetType to determine the type of annotation.

COM applications must call this method before calling Annotation::IGetAttachedEntities or Annotation::IGetAttachedEntityTypes. Dispatch applications do not need a count method because they can use the upper SafeArray bound from the Annotation::GetAttachedEntities and Annotation::GetAttachedEntityTypes return values to determine the array size.
