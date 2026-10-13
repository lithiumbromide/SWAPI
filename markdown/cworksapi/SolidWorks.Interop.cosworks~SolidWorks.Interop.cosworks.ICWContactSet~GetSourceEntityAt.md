---
title: "GetSourceEntityAt Method (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "GetSourceEntityAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetSourceEntityAt.html"
---

# GetSourceEntityAt Method (ICWContactSet)

Gets the entity type and source entity of this contact set at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSourceEntityAt( _
   ByVal NIndex As System.Integer, _
   ByRef NSel As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim NIndex As System.Integer
Dim NSel As System.Integer
Dim value As System.Object

value = instance.GetSourceEntityAt(NIndex, NSel)
```

### C#

```csharp
System.object GetSourceEntityAt(
   System.int NIndex,
   out System.int NSel
)
```

### C++/CLI

```cpp
System.Object^ GetSourceEntityAt(
   System.int NIndex,
   [Out] System.int NSel
)
```

### Parameters

- `NIndex`: 0-based index of the entity
- `NSel`: Type of entity (see **Remarks**)

### Return Value

Entity

## VBA Syntax

See [CWContactSet::GetSourceEntityAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~GetSourceEntityAt.html).

## Remarks

Before calling this method, call [ICWContactSet::SourceEntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~SourceEntityCount.html) to get the value of NIndex.

Faces, edges, and vertices are allowed as source entities. See [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) in the SOLIDWORKS API Enumerations Help for their types.

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::RemoveSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveSourceEntity.html)
[ICWContactSet::RemoveTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~RemoveTargetEntity.html)
[ICWContactSet::TargetEntityCount Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~TargetEntityCount.html)
[ICWContactSet::GetTargetEntityAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~GetTargetEntityAt.html)
[ICWContactSet::InsertSourceEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertSourceEntity.html)
[ICWContactSet::InsertTargetEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~InsertTargetEntity.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
