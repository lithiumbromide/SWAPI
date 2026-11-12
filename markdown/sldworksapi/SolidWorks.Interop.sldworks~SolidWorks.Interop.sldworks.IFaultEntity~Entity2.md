---
title: "Entity2 Property (IFaultEntity)"
project: "SOLIDWORKS API Help"
interface: "IFaultEntity"
member: "Entity2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity2.html"
---

# Entity2 Property (IFaultEntity)

Gets the specified entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Entity2( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFaultEntity
Dim Index As System.Integer
Dim value As System.Object

value = instance.Entity2(Index)
```

### C#

```csharp
System.object Entity2(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.Object^ Entity2 {
   System.Object^ get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index number indicating the entity to get

### Property Value

Entity at Index or NULL if the object at Index is not an entity

## VBA Syntax

See [FaultEntity::Entity2](ms-its:sldworksapivb6.chm::/sldworks~FaultEntity~Entity2.html).

## Remarks

To determine the value for Index, call [IFaultEntity::Count](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~Count.html) before calling this property. Call [IFaultEntity::ErrorCode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity~ErrorCode.html) to determine the error code.

This method might return NULL if the entity is absorbed by the fault.

## See Also

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.html)
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
