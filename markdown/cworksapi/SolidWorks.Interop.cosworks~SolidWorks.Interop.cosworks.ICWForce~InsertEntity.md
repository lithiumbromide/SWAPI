---
title: "InsertEntity Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~InsertEntity.html"
---

# InsertEntity Method (ICWForce)

Adds an entity to the set of entities to which to apply this force or torque.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim DispEntity As System.Object

instance.InsertEntity(DispEntity)
```

### C#

```csharp
void InsertEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity to which this force or torque is applied (see **Remarks**)

## VBA Syntax

See [CWForce::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~InsertEntity.html).

## Remarks

| If this force's direction is... | Then specify DispEntity with... |
| --- | --- |
| Normal | Face or shell edge. |
| In a selected direction | Face, edge, vertex, or reference point. Call ICWForce::SetReferenceGeometry to specify the direction reference. |

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
