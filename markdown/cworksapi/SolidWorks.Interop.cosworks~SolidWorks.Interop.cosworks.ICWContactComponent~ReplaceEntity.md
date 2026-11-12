---
title: "ReplaceEntity Method (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "ReplaceEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ReplaceEntity.html"
---

# ReplaceEntity Method (ICWContactComponent)

Replaces the entity of this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReplaceEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
Dim DispEntity As System.Object

instance.ReplaceEntity(DispEntity)
```

### C#

```csharp
void ReplaceEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void ReplaceEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Replacing component

## VBA Syntax

See [CWContactComponent::ReplaceEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~ReplaceEntity.html).

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactComponent::InsertEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~InsertEntity.html)
[ICWContactComponent::RemoveEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
