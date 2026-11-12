---
title: "SourceEntityCount Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "SourceEntityCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~SourceEntityCount.html"
---

# SourceEntityCount Property (ICWContactSet)

Gets the number of source entities in this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SourceEntityCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

value = instance.SourceEntityCount
```

### C#

```csharp
System.int SourceEntityCount {get;}
```

### C++/CLI

```cpp
property System.int SourceEntityCount {
   System.int get();
}
```

### Property Value

Number of source entities

## VBA Syntax

See [CWContactSet::SourceEntityCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~SourceEntityCount.html).

## Requirements

Call this method before calling [ICWContactSet::GetSourceEntityAt](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html) and [ICWContactSet::RemoveSourceEntity](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~RemoveSourceEntity.html) to determine a valid index for each method.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::GetTargetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html)
[ICWContactSet::InsertSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertSourceEntity.html)
[ICWContactSet::InsertTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertTargetEntity.html)
[ICWContactSet::RemoveTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveTargetEntity.html)
[ICWContactSet::TargetEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TargetEntityCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
