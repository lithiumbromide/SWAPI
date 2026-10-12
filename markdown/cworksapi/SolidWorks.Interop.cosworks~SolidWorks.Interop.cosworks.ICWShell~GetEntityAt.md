---
title: "GetEntityAt Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "GetEntityAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetEntityAt.html"
---

# GetEntityAt Method (ICWShell)

Gets the entity at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityAt( _
   ByVal NIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim NIndex As System.Integer
Dim value As System.Object

value = instance.GetEntityAt(NIndex)
```

### C#

```csharp
System.object GetEntityAt(
   System.int NIndex
)
```

### C++/CLI

```cpp
System.Object^ GetEntityAt(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of entity

### Return Value

Entity or NULL if an entity does not exist at the specified index

## VBA Syntax

See [CWShell::GetEntityAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~GetEntityAt.html).

## Remarks

Before calling this method, call [ICWShell::EntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell~EntityCount.html) to get NIndex.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
