---
title: "InsertEntity Method (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~InsertEntity.html"
---

# InsertEntity Method (ICWContactComponent)

Inserts a component into this contact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
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

- `DispEntity`: Component to insert

## VBA Syntax

See [CWContactComponent::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~InsertEntity.html).

## Remarks

This method is valid only if [ICWContactComponent::GlobalContact](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~GlobalContact.html) is set to 0.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactComponent::RemoveEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~RemoveEntity.html)
[ICWContactComponent::ReplaceEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~ReplaceEntity.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
