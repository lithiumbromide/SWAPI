---
title: "Diagnose Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Diagnose"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Diagnose.html"
---

# Diagnose Method (IBody2)

Gets the [IDiagnoseResult](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult.html) object for this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function Diagnose() As DiagnoseResult
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As DiagnoseResult

value = instance.Diagnose()
```

### C#

```csharp
DiagnoseResult Diagnose()
```

### C++/CLI

```cpp
DiagnoseResult^ Diagnose();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IDiagnoseResult](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult.html) object

## VBA Syntax

See [Body2::Diagnose](ms-its:sldworksapivb6.chm::/sldworks~Body2~Diagnose.html).

## Examples

[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## Remarks

Use the [IDiagnoseResult](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult.html) object to get the gaps and coedges in each gap on this body.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12
