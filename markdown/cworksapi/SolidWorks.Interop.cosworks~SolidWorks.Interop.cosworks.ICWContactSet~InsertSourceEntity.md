---
title: "InsertSourceEntity Method (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "InsertSourceEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertSourceEntity.html"
---

# InsertSourceEntity Method (ICWContactSet)

Inserts the specified source entity into this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSourceEntity( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim DispEntity As System.Object

instance.InsertSourceEntity(DispEntity)
```

### C#

```csharp
void InsertSourceEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertSourceEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity (see **Remarks**)

## VBA Syntax

See [CWContactSet::InsertSourceEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~InsertSourceEntity.html).

## Remarks

Faces, edges, and vertices are allowed as source entities. See [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) in the SOLIDWORKS API Enumerations Help for their types.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::GetSourceEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetSourceEntityAt.html)
[ICWContactSet::GetTargetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html)
[ICWContactSet::RemoveSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveSourceEntity.html)
[ICWContactSet::RemoveTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveTargetEntity.html)
[ICWContactSet::SourceEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~SourceEntityCount.html)
[ICWContactSet::TargetEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TargetEntityCount.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
