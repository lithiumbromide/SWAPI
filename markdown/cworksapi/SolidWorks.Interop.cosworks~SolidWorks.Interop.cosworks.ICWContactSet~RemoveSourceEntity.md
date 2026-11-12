---
title: "RemoveSourceEntity Method (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "RemoveSourceEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveSourceEntity.html"
---

# RemoveSourceEntity Method (ICWContactSet)

Removes a source entity at the specified index from this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveSourceEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim NIndex As System.Integer

instance.RemoveSourceEntity(NIndex)
```

### C#

```csharp
void RemoveSourceEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveSourceEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: 0-based index of entity

## VBA Syntax

See [CWContactSet::RemoveSourceEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~RemoveSourceEntity.html).

## Remarks

Before calling this method, call [ICWContactSet::SourceEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~SourceEntityCount.html) to get the value of NIndex.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::GetSourceEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetSourceEntityAt.html)
[ICWContactSet::GetTargetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html)
[ICWContactSet::InsertSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertSourceEntity.html)
[ICWContactSet::InsertTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertTargetEntity.html)
[ICWContactSet::RemoveTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveTargetEntity.html)
[ICWContactSet::TargetEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TargetEntityCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
