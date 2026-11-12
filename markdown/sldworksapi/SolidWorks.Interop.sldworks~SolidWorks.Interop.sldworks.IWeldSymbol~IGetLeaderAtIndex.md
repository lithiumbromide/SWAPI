---
title: "IGetLeaderAtIndex Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "IGetLeaderAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetLeaderAtIndex.html"
---

# IGetLeaderAtIndex Method (IWeldSymbol)

Gets information about the specified leader on this symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLeaderAtIndex( _
   ByVal Index As System.Integer, _
   ByRef PointCount As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim PointCount As System.Integer
Dim value As System.Double

value = instance.IGetLeaderAtIndex(Index, PointCount)
```

### C#

```csharp
System.double IGetLeaderAtIndex(
   System.int Index,
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.double IGetLeaderAtIndex(
   System.int Index,
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of leader
- `PointCount`: Number of (x,y,z) points returned in the array

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

There can be 0, 1 or 2 lines used with the leader line. If the weld symbol is not attached, then there are 0 lines; otherwise, you can have a straight leaderline (1 line) or a bent leaderline (2 lines). You must infer the number of leaderlines based on IsAttached() and HasExtraLeader().

- IsAttached() == false implies no leaderline and no leaderline points (PointCount=0).
- HasExtraLeader() == false means that this is a straight leaderline and 1 line (PointCount=2)
- HasExtraLeader() == true means that this is a bent leaderline and 2 lines (PointCount=3)

Format of return information is the following array of doubles:

retval[0] = x-coordinate of first leader point

retval[1] = y-coordinate of first leader point

retval[2] = z-coordinate of first leader point

retval[3] = x-coordinate of second leader point

retval[4] = y-coordinate of second leader point

retval[5] = z-coordinate of second leader point

retval[6] = x-coordinate of third leader point

retval[7] = y-coordinate of third leader point

retval[8] = z-coordinate of third leader point

Use [IWeldSymbol::GetLeaderCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetLeaderCount.html) to see how many leaders there are on the weld symbol.

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetLeaderAtIndex.html)
[IWeldSymbol::HasExtraLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~HasExtraLeader.html)
