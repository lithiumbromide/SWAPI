---
title: "GetGapsCount Method (IDiagnoseResult)"
project: "SOLIDWORKS API Help"
interface: "IDiagnoseResult"
member: "GetGapsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetGapsCount.html"
---

# GetGapsCount Method (IDiagnoseResult)

Gets the number of gaps on the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGapsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDiagnoseResult
Dim value As System.Integer

value = instance.GetGapsCount()
```

### C#

```csharp
System.int GetGapsCount()
```

### C++/CLI

```cpp
System.int GetGapsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of gaps

## VBA Syntax

See [DiagnoseResult::GetGapsCount](ms-its:sldworksapivb6.chm::/sldworks~DiagnoseResult~GetGapsCount.html).

## Examples

[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## Remarks

Call this method before calling [IDiagnoseResult::GetCoEdgesAtGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~GetCoEdgesAtGap.html) and [IDiagnoseResult::IGetCoEdgesAtGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.html).

## See Also

[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.html)
[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
