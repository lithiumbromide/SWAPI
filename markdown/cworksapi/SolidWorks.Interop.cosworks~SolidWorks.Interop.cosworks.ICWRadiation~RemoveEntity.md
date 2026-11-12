---
title: "RemoveEntity Method (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~RemoveEntity.html"
---

# RemoveEntity Method (ICWRadiation)

Removes the entity at the specified index from this radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
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

- `NIndex`: 0-based index of entity to remove

## VBA Syntax

See [CWRadiation::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~RemoveEntity.html).

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiation::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~InsertEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
