---
title: "Entity Property (IFaultEntity)"
project: "SOLIDWORKS API Help"
interface: "IFaultEntity"
member: "Entity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity.html"
---

# Entity Property (IFaultEntity)

Obsolete. Superseded by [IFaultEntity::Entity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~Entity2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Entity( _
   ByVal Index As System.Integer _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IFaultEntity
Dim Index As System.Integer
Dim value As Entity

value = instance.Entity(Index)
```

### C#

```csharp
Entity Entity(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property Entity^ Entity {
   Entity^ get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [FaultEntity::Entity](ms-its:sldworksapivb6.chm::/sldworks~FaultEntity~Entity.html).

## See Also

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.html)
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.html)
