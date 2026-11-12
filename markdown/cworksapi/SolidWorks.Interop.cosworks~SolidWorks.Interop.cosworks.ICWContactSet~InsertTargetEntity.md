---
title: "InsertTargetEntity Method (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "InsertTargetEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertTargetEntity.html"
---

# InsertTargetEntity Method (ICWContactSet)

Inserts the specified target entity into this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertTargetEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim DispEntity As System.Object

instance.InsertTargetEntity(DispEntity)
```

### C#

```csharp
void InsertTargetEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertTargetEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity (see **Remarks**)

## VBA Syntax

See [CWContactSet::InsertTargetEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~InsertTargetEntity.html).

## Remarks

Faces, edges, and vertices are allowed as target entities. See [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) in the SOLIDWORKS API Enumerations Help for their types.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::GetSourceEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetSourceEntityAt.html)
[ICWContactSet::GetTargetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html)
[ICWContactSet::InsertSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertSourceEntity.html)
[ICWContactSet::RemoveSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveSourceEntity.html)
[ICWContactSet::RemoveTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveTargetEntity.html)
[ICWContactSet::SourceEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~SourceEntityCount.html)
[ICWContactSet::TargetEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TargetEntityCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
