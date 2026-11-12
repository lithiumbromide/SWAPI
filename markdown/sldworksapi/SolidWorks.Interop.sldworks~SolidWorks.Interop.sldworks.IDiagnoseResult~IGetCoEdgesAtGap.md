---
title: "IGetCoEdgesAtGap Method (IDiagnoseResult)"
project: "SOLIDWORKS API Help"
interface: "IDiagnoseResult"
member: "IGetCoEdgesAtGap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.html"
---

# IGetCoEdgesAtGap Method (IDiagnoseResult)

Gets the coedges at the specified gap.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoEdgesAtGap( _
   ByVal Index As System.Integer, _
   ByVal CoEdgeCount As System.Integer _
) As CoEdge
```

### Visual Basic (Usage)

```vb
Dim instance As IDiagnoseResult
Dim Index As System.Integer
Dim CoEdgeCount As System.Integer
Dim value As CoEdge

value = instance.IGetCoEdgesAtGap(Index, CoEdgeCount)
```

### C#

```csharp
CoEdge IGetCoEdgesAtGap(
   System.int Index,
   System.int CoEdgeCount
)
```

### C++/CLI

```cpp
CoEdge^ IGetCoEdgesAtGap(
   System.int Index,
   System.int CoEdgeCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index number of the gap to get
- `CoEdgeCount`: Number of coedges at that gap

### Return Value

- in-process, unmanaged C++: Pointer to an array of [ICoEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call:

- [IDiagnoseResult::GetGapsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~GetGapsCount.html) before calling this method to determine the index number of the gap to get on this body.
- [IDiagnoseResult::GetCoEdgesCountAtGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~GetCoEdgesCountAtGap.html) before calling this method to get the number of coedges at the gap on this body.

## See Also

[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.html)
[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
