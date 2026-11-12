---
title: "GetLeaderAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetLeaderAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderAtIndex.html"
---

# GetLeaderAtIndex Method (ISFSymbol)

Gets information about the specified leader on this surface finish symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISFSymbol
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLeaderAtIndex(Index)
```

### C#

```csharp
System.object GetLeaderAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLeaderAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of leader

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [SFSymbol::GetLeaderAtIndex](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetLeaderAtIndex.html).

## Remarks

There can be 0, 1 or 2 lines used with the leader line. If the surface-finish sysmbol is not attached then, there are 0 lines; otherwise, you can have a straight leaderline (1 line) or a bent leaderline (2 lines). You must infer the number of leader lines based on [ISFSymbol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~IsAttached.html) and [ISFSymbol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~HasExtraLeader.html).

- ISFSymbol::IsAttached == false implies no leaderline and no leaderline points (PointCount=0).
- ISFSymbol::HasExtraLeader == false means that this is a straight leaderline and 1 line (PointCount=2)
- ISFSymbol::HasExtraLeader == true means that this is a bent leaderline and 2 lines (PointCount=3)

Format of return information is the following array of doubles:

|  | retval [0] = x-coordinate of first leader point |
| --- | --- |
|  | retval [1] = y-coordinate of first leader point |
|  | retval [2] = z-coordinate of first leader point |
|  |  |
|  | retval [3] = x-coordinate of second leader point |
|  | retval [4] = y-coordinate of second leader point |
|  | retval [5] = z-coordinate of second leader point |
|  |  |
|  | retval [6] = x-coordinate of third leader point |
|  | retval [7] = y-coordinate of third leader point |
|  | retval [8] = z-coordinate of third leader point |

Use [ISFSymbol::GetLeaderCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetLeaderCount.html) to see how many leaders there are on the [ISFSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html) object.

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetLeaderAtIndex.html)
