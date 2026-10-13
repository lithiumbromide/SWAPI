---
title: "GetEntityAt2 Method (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "GetEntityAt2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~GetEntityAt2.html"
---

# GetEntityAt2 Method (ICWMeshControl)

Obsolete. Superseded by [ICWMeshControl::GetEntityAt3](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~GetEntityAt3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityAt2( _
   ByVal NIndex As System.Integer, _
   ByVal BExcludeVertexAndReference As System.Integer, _
   ByRef NSelectionType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim NIndex As System.Integer
Dim BExcludeVertexAndReference As System.Integer
Dim NSelectionType As System.Integer
Dim value As System.Object

value = instance.GetEntityAt2(NIndex, BExcludeVertexAndReference, NSelectionType)
```

### C#

```csharp
System.object GetEntityAt2(
   System.int NIndex,
   System.int BExcludeVertexAndReference,
   out System.int NSelectionType
)
```

### C++/CLI

```cpp
System.Object^ GetEntityAt2(
   System.int NIndex,
   System.int BExcludeVertexAndReference,
   [Out] System.int NSelectionType
)
```

### Parameters

- `NIndex`: 0-based index of entity
- `BExcludeVertexAndReference`: True to exclude the vertex and reference, false to not
- `NSelectionType`: Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Entity

## VBA Syntax

See [CWMeshControl::GetEntityAt2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~GetEntityAt2.html).

## Remarks

To specify NIndex, use [ICWMeshControl::EntityCount](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~EntityCount.html) to determine the number of entities in this mesh control.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::InsertEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~InsertEntity.html)
[ICWMeshControl::RemoveEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2017 SP2
