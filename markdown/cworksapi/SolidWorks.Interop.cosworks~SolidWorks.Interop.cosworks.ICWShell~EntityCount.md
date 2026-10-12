---
title: "EntityCount Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "EntityCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~EntityCount.html"
---

# EntityCount Property (ICWShell)

Gets the number of entities in the shell.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property EntityCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
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

Number of entities in the shell

## VBA Syntax

See [CWShell::EntityCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~EntityCount.html).

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::GetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetEntityAt.html)
[ICWShell::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
