---
title: "Annotation::GetAttachedEntities"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetAttachedEntities.htm"
---

# Annotation::GetAttachedEntities

This method is obsolete and has been superseded by [Annotation::GetAttachedEntities2](Annotation__GetAttachedEntities2.htm).

Description

This method returns the entities associated with this annotation.

Syntax (OLE Automation)

retval = Annotation.GetAttachedEntities ( )

| Return: | (VARIANT) retval | Pointer to an array of Dispatch objects |
| --- | --- | --- |

Syntax (COM)

status = Annotation->IGetAttachedEntities ( retval )

| Output: | (LPUNKNOWN*) retval | Pointer to an array of LPUNKNOWN objects |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful; S_FALSE otherwise |

Remarks

This method now supports all annotation types. In SolidWorks 99, datecode 1999207, support was only available for cosmetic thread annotations and surface finish symbol annotations (swCThread and swSFSymbol, respectively). See Annotation::GetType to determine the type of annotation.

The array returned by this function may contain one or more objects of varying type. To determine the corresponding object type in the Annotation::GetAttachedEntites array, see Annotation::GetAttachedEntityTypes. COM applications can use QueryInterface to obtain the specific object from the LPUNKNOWN pointer.

| Object Type | Object Returned |
| --- | --- |
| swSelFACES | Face2 |
| swSelEDGES | Edge |
| swSelVERTICES | Vertex |
| swSelSKETCHSEGS | SketchSegment |
| swSelSKETCHPOINTS | SketchPoint |
| swSelNOTHING | NULL (annotation is dangling or unsupported) |

You can associate annotations with some items not listed in the previous table (for example, origins). If this annotation is attached to one or more of those entities, then SolidWorks returns a corresponding NULL in one of the array positions and Annotation::GetAttachedEntityTypes indicates the unsupported entity by returning a corresponding swSelNOTHING value. COM applications that call Annotation::IGetAttachedEntityCount include the NULL value in the total count of associated entities.

Likewise, if an annotation has become disassociated from its geometry, then SolidWorks returns a corresponding NULL in one of the array positions and Annotation::GetAttachedEntityTypes indicates the dangling item by returning a corresponding swSelNOTHING value.

COM applications must call Annotation::IGetAttachedEntityCount before calling this this method. Annotation::IGetAttachedEntityCount determines the necessary array size in your call to Annotation::IGetAttachedEntities and creates the list of attached entities. Dispatch applications can determine the number of associated entities by checking the size of the SafeArray.

If this annotation is not associated with any geometry (for example, a note without a leaderline), then SolidWorks returns an empty array. See Return Values for details on detecting empty arrays.
