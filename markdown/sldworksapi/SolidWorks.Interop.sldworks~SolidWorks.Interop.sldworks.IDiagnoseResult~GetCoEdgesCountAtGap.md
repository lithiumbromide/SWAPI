---
title: "GetCoEdgesCountAtGap Method (IDiagnoseResult)"
project: "SOLIDWORKS API Help"
interface: "IDiagnoseResult"
member: "GetCoEdgesCountAtGap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesCountAtGap.html"
---

# GetCoEdgesCountAtGap Method (IDiagnoseResult)

Gets the number of coedges at the specified gap.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCoEdgesCountAtGap( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDiagnoseResult
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetCoEdgesCountAtGap(Index)
```

### C#

```csharp
System.int GetCoEdgesCountAtGap(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetCoEdgesCountAtGap(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index number of the gap to get

### Return Value

Number of coedges at that gap

## VBA Syntax

See [DiagnoseResult::GetCoEdgesCountAtGap](ms-its:sldworksapivb6.chm::/sldworks~DiagnoseResult~GetCoEdgesCountAtGap.html).

## Examples

Call this method before calling [IDiagnoseResult::IGetCoEdgesAtGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.html).

## See Also

[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.html)
[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
