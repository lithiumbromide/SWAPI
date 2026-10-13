---
title: "Check Property (IEdge)"
project: "SOLIDWORKS API Help"
interface: "IEdge"
member: "Check"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Check.html"
---

# Check Property (IEdge)

Gets whether the edge is a valid, and, if not, returns the faults.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Check As FaultEntity
```

### Visual Basic (Usage)

```vb
Dim instance As IEdge
Dim value As FaultEntity

value = instance.Check
```

### C#

```csharp
FaultEntity Check {get;}
```

### C++/CLI

```cpp
property FaultEntity^ Check {
   FaultEntity^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to [IFaultEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity.html) object

## VBA Syntax

See [Edge::Check](ms-its:sldworksapivb6.chm::/sldworks~Edge~Check.html).

## Examples

[Check Edges for Faults (C#)](Check_Edges_for_Faults_Example_CSharp.htm)
[Check Edges for Faults (VB.NET)](Check_Edges_for_Faults_Example_VBNET.htm)
[Check Edges for Faults (VBA)](Check_Edges_for_Faults_Example_VB.htm)

## See Also

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html)
[IFace2::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Check.html)
[IBody2::Check3 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
