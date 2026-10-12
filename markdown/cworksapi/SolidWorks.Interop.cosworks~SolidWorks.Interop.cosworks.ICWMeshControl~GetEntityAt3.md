---
title: "GetEntityAt3 Method (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "GetEntityAt3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~GetEntityAt3.html"
---

# GetEntityAt3 Method (ICWMeshControl)

Gets the entity at the specified index for this mesh control.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityAt3( _
   ByVal NIndex As System.Integer, _
   ByVal BExcludeVertexAndReference As System.Boolean, _
   ByRef NSelectionType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
Dim NIndex As System.Integer
Dim BExcludeVertexAndReference As System.Boolean
Dim NSelectionType As System.Integer
Dim value As System.Object

value = instance.GetEntityAt3(NIndex, BExcludeVertexAndReference, NSelectionType)
```

### C#

```csharp
System.object GetEntityAt3(
   System.int NIndex,
   System.bool BExcludeVertexAndReference,
   out System.int NSelectionType
)
```

### C++/CLI

```cpp
System.Object^ GetEntityAt3(
   System.int NIndex,
   System.bool BExcludeVertexAndReference,
   [Out] System.int NSelectionType
)
```

### Parameters

- `NIndex`: 0-based index of entity
- `BExcludeVertexAndReference`: -1 or true to exclude the vertex and reference, 0 or false to not
- `NSelectionType`: Type of entity as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Entity

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
