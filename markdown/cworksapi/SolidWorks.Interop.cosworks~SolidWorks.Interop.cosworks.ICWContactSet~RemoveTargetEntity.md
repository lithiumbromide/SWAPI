---
title: "RemoveTargetEntity Method (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "RemoveTargetEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveTargetEntity.html"
---

# RemoveTargetEntity Method (ICWContactSet)

Removes a target entity at the specified index from this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveTargetEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim NIndex As System.Integer

instance.RemoveTargetEntity(NIndex)
```

### C#

```csharp
void RemoveTargetEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveTargetEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of entity

## VBA Syntax

See [CWContactSet::RemoveTargetEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~RemoveTargetEntity.html).

## Remarks

Before calling this method, call [ICWContactSet::TargetEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~TargetEntityCount.html) to get the value of NIndex.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::GetSourceEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetSourceEntityAt.html)
[ICWContactSet::GetTargetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html)
[ICWContactSet::InsertSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertSourceEntity.html)
[ICWContactSet::InsertTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertTargetEntity.html)
[ICWContactSet::RemoveSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveSourceEntity.html)
[ICWContactSet::SourceEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~SourceEntityCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
