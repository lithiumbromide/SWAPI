---
title: "GetAttachedEntities3 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetAttachedEntities3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3.html"
---

# GetAttachedEntities3 Method (IAnnotation)

Gets the entities to which this annotation is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachedEntities3() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

value = instance.GetAttachedEntities3()
```

### C#

```csharp
System.object GetAttachedEntities3()
```

### C++/CLI

```cpp
System.Object^ GetAttachedEntities3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of objects

## VBA Syntax

See [Annotation::GetAttachedEntities3](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetAttachedEntities3.html).

## Examples

[Get Types of Entities Attached to Selected Annotation (VBA)](Get_Types_of_Entities_for_Selected_Dimension_Example_VB.htm)
[Get Types of Entities Attached to Selected Annotation (VB.NET)](Get_Types_of_Entities_for_Selected_Dimension_Example_VBNET.htm)
[Get Types of Entities Attached to Selected Annotation (C#)](Get_Types_of_Entities_for_Selected_Dimension_Example_CSharp.htm)
[Select Silhouette Edge Attached to Note (C#)](Select_Silhouette_Edge_Attached_to_Note_Example_CSharp.htm)
[Select Silhouette Edge Attached to Note (VB.NET)](Select_Silhouette_Edge_Attached_to_Note_Example_VBNET.htm)
[Select Silhouette Edge Attached to Note (VBA)](Select_Silhouette_Edge_Attached_to_Note_Example_VB.htm)
[Attach Annotation to Entity (C#)](Attach_Annotation_to_Entity_Example_CSharp.htm)
[Attach Annotation to Entity (VB.NET)](Attach_Annotation_to_Entity_Example_VBNET.htm)
[Attach Annotation to Entity (VBA)](Attach_Annotation_to_Entity_Example_VB.htm)

## Remarks

This method now supports all annotation types. See [IAnnotation::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetType.html) to determine the type of annotation.

The array returned by this function may contain one or more objects of varying type. To determine the corresponding object type in the IAnnotation::GetAttachedEntites3 array, see [IAnnotation::GetAttachedEntityTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.html) or [IAnnotation::IGetAttachedEntityTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetAttachedEntityTypes.html). COM applications can use QueryInterface to obtain the specific object from the LPUNKNOWN pointer.

| Object Type | Object Returned |
| --- | --- |
| swSelFACES | IFace2 |
| swSelEDGES | IEdge |
| swSelVERTICES | IVertex |
| swSelSKETCHSEGS | ISketchSegment |
| swSelSKETCHPOINTS | ISketchPoint |
| swSelSilhouettes | ISilhouetteEdge |
| swSelNOTHING | NULL (annotation is dangling or unsupported) |

You can associate annotations with some items not listed in the previous table (for example, origins). If this annotation is attached to one or more of those entities, then SOLIDWORKS returns a corresponding NULL in one of the array positions and IAnnotation::GetAttachedEntityTypes indicates the unsupported entity by returning a corresponding swSelNOTHING value. COM applications that call [IAnnotation::GetAttachedEntityCount3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntityCount3.html) include the NULL value in the total count of associated entities.

Likewise, if an annotation has become disassociated from its geometry, then SOLIDWORKS returns a corresponding NULL in one of the array positions and [IAnnotation::GetAttachedEntityTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.html) indicates the dangling item by returning a corresponding swSelNOTHING value.

If this annotation is not associated with any geometry (for example, a note without a leaderline), then SOLIDWORKS returns an empty array.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.html)
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.html)
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
