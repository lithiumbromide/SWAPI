---
title: "GetEntityAt Method (ICWLoadsAndRestraints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraints"
member: "GetEntityAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints~GetEntityAt.html"
---

# GetEntityAt Method (ICWLoadsAndRestraints)

Gets the entity at the specified index in this load or restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityAt( _
   ByVal NIndex As System.Integer, _
   ByRef NSelType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraints
Dim NIndex As System.Integer
Dim NSelType As System.Integer
Dim value As System.Object

value = instance.GetEntityAt(NIndex, NSelType)
```

### C#

```csharp
System.object GetEntityAt(
   System.int NIndex,
   out System.int NSelType
)
```

### C++/CLI

```cpp
System.Object^ GetEntityAt(
   System.int NIndex,
   [Out] System.int NSelType
)
```

### Parameters

- `NIndex`: 0-based index of entity
- `NSelType`: Entity type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Entity

## VBA Syntax

See [CWLoadsAndRestraints::GetEntityAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraints~GetEntityAt.html).

## Remarks

Call [ICWLoadsAndRestraints::EntityCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraints~EntityCount.html) before calling this method to get a valid value for NIndex.

## See Also

[ICWLoadsAndRestraints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html)
[ICWLoadsAndRestraints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
