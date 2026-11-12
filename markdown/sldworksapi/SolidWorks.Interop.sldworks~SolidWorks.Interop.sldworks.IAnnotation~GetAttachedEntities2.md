---
title: "GetAttachedEntities2 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetAttachedEntities2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.html"
---

# GetAttachedEntities2 Method (IAnnotation)

Obsolete. Superseded by [IAnnotation::GetAttachedEntities3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntities3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttachedEntities2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

value = instance.GetAttachedEntities2()
```

### C#

```csharp
System.object GetAttachedEntities2()
```

### C++/CLI

```cpp
System.Object^ GetAttachedEntities2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of objects

## VBA Syntax

See [Annotation::GetAttachedEntities2](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetAttachedEntities2.html).

## Examples

[Get Types of Entities for Selected Dimension (VBA)](Get_Types_of_Entities_for_Selected_Dimension_Example_VB.htm)
[Get BOM Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)
[Get BOM Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)
[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)

## Remarks

This method now supports all annotation types. See [IAnnotation::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetType.html) to determine the type of annotation.

The array returned by this function may contain one or more objects of varying type. To determine the corresponding object type in the IAnnotation::GetAttachedEntites2 array, see [IAnnotation::GetAttachedEntityTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.html). COM applications can use QueryInterface to obtain the specific object from the LPUNKNOWN pointer.

| Object Type | Object Returned |
| --- | --- |
| swSelFACES | IFace2 |
| swSelEDGES | IEdge |
| swSelVERTICES | IVertex |
| swSelSKETCHSEGS | ISketchSegment |
| swSelSKETCHPOINTS | ISketchPoint |
| swSelNOTHING | NULL (annotation is dangling or unsupported) |

You can associate annotations with some items not listed in the previous table (for example, origins). If this annotation is attached to one or more of those entities, then SOLIDWORKS returns a corresponding NULL in one of the array positions and IAnnotation::GetAttachedEntityTypes indicates the unsupported entity by returning a corresponding swSelNOTHING value. COM applications that call [IAnnotation::GetAttachedEntityCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntityCount2.html) include the NULL value in the total count of associated entities.

Likewise, if an annotation has become disassociated from its geometry, then SOLIDWORKS returns a corresponding NULL in one of the array positions and [IAnnotation::GetAttachedEntityTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.html) indicates the dangling item by returning a corresponding swSelNOTHING value.

If this annotation is not associated with any geometry (for example, a note without a leaderline), then SOLIDWORKS returns an empty array.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetAttachedEntityCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount2.html)
[IAnnotation::GetAttachedEntityTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.html)
[IAnnotation::GetNext3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.html)
[IAnnotation::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.html)
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.html)
[IAttribute::GetEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.html)
[IAttribute::IGetEntity2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.html)
[IAttribute::GetEntityState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.html)
[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity::GetSafeEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity.html)
[IFaultEntity::Entity2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity2.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.html)
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.html)
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html)
[IAnnotation::SetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.html)
[IAnnotation::ISetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
