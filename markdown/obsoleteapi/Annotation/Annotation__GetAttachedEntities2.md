---
title: "Annotation::GetAttachedEntities2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetAttachedEntities2.htm"
---

# Annotation::GetAttachedEntities2

This method is obsolete and has been superseded by [Annotation::GetAttachedEntities3](sldworksAPI.chm::/Annotation/Annotation__GetAttachedEntities3.htm).

Description

This method gets the entities to which this annotation is attached.

Syntax (OLE Automation)

retval = Annotation.GetAttachedEntities2 ()

| Output: | (VARIANT) retval | Pointer to an array of Dispatch objects |
| --- | --- | --- |

Syntax (COM)

status = Annotation->GetAttachedEntities2 ( &retval)

| Output: | (VARIANT) retval | Pointer to an array of LPUNKNOWN objects |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method now supports all annotation types. See Annotation::GetType to determine the type of annotation.

The array returned by this function may contain one or more objects of varying type. To determine the corresponding object type in the Annotation::GetAttachedEntites2 array, see Annotation::GetAttachedEntityTypes. COM applications can use QueryInterface to obtain the specific object from the LPUNKNOWN pointer.

| Object Type | Object Returned |
| --- | --- |
| swSelFACES | Face2 |
| swSelEDGES | Edge |
| swSelVERTICES | Vertex |
| swSelSKETCHSEGS | SketchSegment |
| swSelSKETCHPOINTS | SketchPoint |
| swSelNOTHING | NULL (annotation is dangling or unsupported) |

You can associate annotations with some items not listed in the previous table (for example, origins). If this annotation is attached to one or more of those entities, then SolidWorks returns a corresponding NULL in one of the array positions and Annotation::GetAttachedEntityTypes indicates the unsupported entity by returning a corresponding swSelNOTHING value. COM applications that call Annotation::GetAttachedEntityCount2 include the NULL value in the total count of associated entities.

Likewise, if an annotation has become disassociated from its geometry, then SolidWorks returns a corresponding NULL in one of the array positions and Annotation::GetAttachedEntityTypes indicates the dangling item by returning a corresponding swSelNOTHING value.

COM applications must call Annotation::GetAttachedEntityCount2 before calling this method. Annotation::GetAttachedEntityCount2 determines the necessary array size in your call to Annotation::GetAttachedEntities2 and creates the list of attached entities. Dispatch applications can determine the number of associated entities by checking the size of the SafeArray.

If this annotation is not associated with any geometry (for example, a note without a leaderline), then SolidWorks returns an empty array. See Return Values for details on detecting empty arrays.
