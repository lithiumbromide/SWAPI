---
title: "Annotation::GetAttachedEntityCount2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetAttachedEntityCount2.htm"
---

# Annotation::GetAttachedEntityCount2

This method is obsolete and has been superseded by [Annotation::GetAttachedEntityCount3](sldworksAPI.chm::/Annotation/Annotation__GetAttachedEntityCount3.htm).

Description

This method gets the number of entities to which this annotation is attached.

Syntax (OLE Automation)

retval = Annotation.GetAttachedEntityCount2 ()

| Output: | (long) retval | Number of entities to which this annotation is attached |
| --- | --- | --- |

Syntax (COM)

status = Annotation->GetAttachedEntityCount2 ( &retval)

| Output: | (long) retval | Number of entities to which this annotation is attached |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method supports all annotation types. See Annotation::GetType to determine the type of annotation.

Call this method before calling the COM versions of Annotation::GetAttachedEntities2 or Annotation::GetAttachedEntityTypes. Dispatch applications do not need a count method because they can use the upper SafeArray bound from the Annotation::GetAttachedEntities2 and Annotation::GetAttachedEntityTypes return values to determine the array size.
