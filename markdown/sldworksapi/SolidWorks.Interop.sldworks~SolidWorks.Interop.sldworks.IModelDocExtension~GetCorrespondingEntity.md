---
title: "GetCorrespondingEntity Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCorrespondingEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html"
---

# GetCorrespondingEntity Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::GetCorrespondingEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorrespondingEntity( _
   ByVal Entity As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Entity As System.Object
Dim value As System.Object

value = instance.GetCorrespondingEntity(Entity)
```

### C#

```csharp
System.object GetCorrespondingEntity(
   System.object Entity
)
```

### C++/CLI

```cpp
System.Object^ GetCorrespondingEntity(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: Dispatch pointer to a [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html), [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), or [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) entity

### Return Value

Dispatch pointer to the corresponding entity in the context of the component

## VBA Syntax

See [ModelDocExtension::GetCorrespondingEntity](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCorrespondingEntity.html).

## Examples

[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)
[Open Part from Assembly (VBA)](Open_Part_from_Assembly_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.html)
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html)
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15.1
