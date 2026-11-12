---
title: "RemoveEntity Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~RemoveEntity.html"
---

# RemoveEntity Method (ICWShell)

Removes the entity at the specified index from the shell.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim NIndex As System.Integer

instance.RemoveEntity(NIndex)
```

### C#

```csharp
void RemoveEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of the entity to remove

## VBA Syntax

See [CWShell::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~RemoveEntity.html).

## Remarks

Before calling this method, call [ICWShell::EntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell~EntityCount.html) to get NIndex.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
