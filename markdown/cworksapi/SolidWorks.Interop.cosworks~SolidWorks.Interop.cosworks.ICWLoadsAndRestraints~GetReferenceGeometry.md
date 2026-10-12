---
title: "GetReferenceGeometry Method (ICWLoadsAndRestraints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraints"
member: "GetReferenceGeometry"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints~GetReferenceGeometry.html"
---

# GetReferenceGeometry Method (ICWLoadsAndRestraints)

Gets the entity used for reference geometry in this load or restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferenceGeometry( _
   ByRef NSelType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraints
Dim NSelType As System.Integer
Dim value As System.Object

value = instance.GetReferenceGeometry(NSelType)
```

### C#

```csharp
System.object GetReferenceGeometry(
   out System.int NSelType
)
```

### C++/CLI

```cpp
System.Object^ GetReferenceGeometry(
   [Out] System.int NSelType
)
```

### Parameters

- `NSelType`: Entity type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

Entity

## VBA Syntax

See [CWLoadsAndRestraints::GetReferenceGeometry](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraints~GetReferenceGeometry.html).

## See Also

[ICWLoadsAndRestraints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html)
[ICWLoadsAndRestraints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
