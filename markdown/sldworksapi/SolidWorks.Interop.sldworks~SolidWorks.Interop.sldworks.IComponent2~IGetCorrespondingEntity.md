---
title: "IGetCorrespondingEntity Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetCorrespondingEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.html"
---

# IGetCorrespondingEntity Method (IComponent2)

Gets the entity that corresponds with the Dispatch pointer in the context of the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCorrespondingEntity( _
   ByVal PEntity As Entity _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim PEntity As Entity
Dim value As Entity

value = instance.IGetCorrespondingEntity(PEntity)
```

### C#

```csharp
Entity IGetCorrespondingEntity(
   Entity PEntity
)
```

### C++/CLI

```cpp
Entity^ IGetCorrespondingEntity(
   Entity^ PEntity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PEntity`: Pointer to the [IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) object (vertex, face, or edge)

### Return Value

Pointer to the corresponding object in the context of the component

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.html)
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html)
[IModelDocExtension::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision number 10.0
