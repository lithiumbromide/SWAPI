---
title: "EntityCount Property (ICWLoadsAndRestraints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraints"
member: "EntityCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints~EntityCount.html"
---

# EntityCount Property (ICWLoadsAndRestraints)

Gets the number of entities in this load or restraint.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property EntityCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraints
Dim value As System.Integer

value = instance.EntityCount
```

### C#

```csharp
System.int EntityCount {get;}
```

### C++/CLI

```cpp
property System.int EntityCount {
   System.int get();
}
```

### Property Value

Number of entities in this load or restraint; does not include reference geometry

## VBA Syntax

See [CWLoadsAndRestraints::EntityCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraints~EntityCount.html).

## Examples

See the [ICWLoadsAndRestraints](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html) examples.

## Remarks

Call this method before calling [ICWLoadAndRestraint::GetEntityAt](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraints~GetEntityAt.html).

## See Also

[ICWLoadsAndRestraints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html)
[ICWLoadsAndRestraints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
