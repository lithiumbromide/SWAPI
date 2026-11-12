---
title: "TargetEntityCount Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "TargetEntityCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TargetEntityCount.html"
---

# TargetEntityCount Property (ICWContactSet)

Gets the number of target entities in this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TargetEntityCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

value = instance.TargetEntityCount
```

### C#

```csharp
System.int TargetEntityCount {get;}
```

### C++/CLI

```cpp
property System.int TargetEntityCount {
   System.int get();
}
```

### Property Value

Number of target entities

## VBA Syntax

See [CWContactSet::TargetEntityCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~TargetEntityCount.html).

## Remarks

Call this method before calling [ICWContactSet::GetTargetEntityAt](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html) and [ICWContactSet::RemoveTargetEntity](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~RemoveTargetEntity.html) to determine a valid index for each method.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::GetSourceEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetSourceEntityAt.html)
[ICWContactSet::InsertTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertTargetEntity.html)
[ICWContactSet::SourceEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~SourceEntityCount.html)
[ICWContactSet::InsertSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertSourceEntity.html)
[ICWContactSet::InsertTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertTargetEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
