---
title: "GetType Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetType.html"
---

# GetType Method (IEntity)

Gets the type of the entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim value As System.Integer

value = instance.GetType()
```

### C#

```csharp
System.int GetType()
```

### C++/CLI

```cpp
System.int GetType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [Entity::GetType](ms-its:sldworksapivb6.chm::/sldworks~Entity~GetType.html).

## Examples

[Get Knit Surface Data (VBA)](Get_Knit_Surface_Data_Example_VB.htm)
[Get Mirror Solid Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)
[Get Component from Feature (VBA)](Get_Component_from_Feature_Example_VB.htm)
[Get Component from Feature (VB.NET)](Get_Component_from_Feature_Example_VBNET.htm)
[Get Component from Feature (C#)](Get_Component_from_Feature_Example_CSharp.htm)

## Remarks

You can use this method to determine the entity type and the appropriate function calls allowed for the specific type. For example, if this entity is a face, you can call [IFace2::GetArea](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetArea.html). However, you cannot call [IEdge::GetCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetCurve.html) or [IEdge::IGetCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~IGetCurve.html) because it is on [IEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) object. COM implementations can also use QueryInterface to determine the underlying interface supported by this [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object.

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.html)
[IAttribute::GetEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.html)
[IAttribute::IGetEntity2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.html)
[IAttribute::GetEntityState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.html)
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html)
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.html)

## Availability

SOLIDWORKS 99, datecode 1999207
