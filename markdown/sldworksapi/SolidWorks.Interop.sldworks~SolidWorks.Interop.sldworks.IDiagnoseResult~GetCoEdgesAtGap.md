---
title: "GetCoEdgesAtGap Method (IDiagnoseResult)"
project: "SOLIDWORKS API Help"
interface: "IDiagnoseResult"
member: "GetCoEdgesAtGap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesAtGap.html"
---

# GetCoEdgesAtGap Method (IDiagnoseResult)

Gets the coedges at the specified gap.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoEdgesAtGap( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDiagnoseResult
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetCoEdgesAtGap(Index)
```

### C#

```csharp
System.object GetCoEdgesAtGap(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetCoEdgesAtGap(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index number of the gap to get

### Return Value

Array of [coedges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html)

## VBA Syntax

See [DiagnoseResult::GetCoEdgesAtGap](ms-its:sldworksapivb6.chm::/sldworks~DiagnoseResult~GetCoEdgesAtGap.html).

## Examples

[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## Remarks

Call [IDiagnoseResult::GetGapsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~GetGapsCount.html) before calling this method to determine the index number of the gap to get on this body.

## See Also

[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.html)
[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.html)
[IDiagnoseResult::GetCoEdgesCountAtGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesCountAtGap.html)
[IDiagnoseResult::IGetCoEdgesAtGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
