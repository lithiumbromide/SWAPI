---
title: "GetCorrespondingEntity Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetCorrespondingEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html"
---

# GetCorrespondingEntity Method (IComponent2)

Gets the entity that corresponds with the Dispatch pointer in the context of the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorrespondingEntity( _
   ByVal Entity As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
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

- `Entity`: Pointer to the Dispatch object of an entity (vertex, face, or edge)

### Return Value

Pointer to the corresponding object in the context of the component

## VBA Syntax

See [Component2::GetCorrespondingEntity](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetCorrespondingEntity.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.html)
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.html)
[IModelDocExtension::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
