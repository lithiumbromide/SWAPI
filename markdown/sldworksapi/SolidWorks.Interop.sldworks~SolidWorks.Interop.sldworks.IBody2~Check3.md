---
title: "Check3 Property (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Check3"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.html"
---

# Check3 Property (IBody2)

Gets whether the body is a valid and returns an [IFaultEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity.html) object if any faults exist.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Check3 As FaultEntity
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As FaultEntity

value = instance.Check3
```

### C#

```csharp
FaultEntity Check3 {get;}
```

### C++/CLI

```cpp
property FaultEntity^ Check3 {
   FaultEntity^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to [IFaultEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaultEntity.html) object

## VBA Syntax

See [Body2::Check3](ms-its:sldworksapivb6.chm::/sldworks~Body2~Check3.html).

## Examples

[Check Bodies for Faults (VBA)](Check_Bodies_for_Faults_Example_VB.htm)
[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IEdge::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Check.html)
[IFace2::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Check.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12
