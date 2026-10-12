---
title: "GetLeaderInfo Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetLeaderInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.html"
---

# GetLeaderInfo Method (IGtol)

Gets information describing the layout of the GTol leader lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderInfo() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim value As System.Object

value = instance.GetLeaderInfo()
```

### C#

```csharp
System.object GetLeaderInfo()
```

### C++/CLI

```cpp
System.Object^ GetLeaderInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetLeaderInfo](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetLeaderInfo.html).

## Remarks

There can be 0, 1 or 2 lines with the leader line. If the GTol is not attached, then there are 0 lines. Otherwise, the GTol can have a straight leaderline (1 line) or a bent leaderline (2 lines). The caller must infer the number of leader lines based on [IGtol::IsAttached](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IsAttached.html) and [IGtol::HasExtraLeader](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~HasExtraLeader.html).

- IGtol::IsAttached() == false implies no leaderline; therefore, there are no leaderline points (PointCount=0).
- IGtol::HasExtraLeader() == false means that this is a straight leaderline; therefore, there is 1 line (PointCount=2).
- IGtol::HasExtraLeader() == True means that this is a bent leaderline; therefore, there are 2 lines (PointCount=3).

The format of return information is the following array of doubles:

`retval`[0] = X-coordinate of first leader point

`retval`[1] = Y-coordinate of first leader point

`retval`[2] = Z-coordinate of first leader point

`retval`[3] = X-coordinate of second leader point

`retval`[4] = Y-coordinate of second leader point

`retval`[5] = Z-coordinate of second leader point

`retval`[6] = X-coordinate of third leader point

`retval`[7] = Y-coordinate of third leader point

`retval`[8] = Z-coordinate of third leader point

Use [IGtol::GetLeaderCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetLeaderCount.html) to see how many leaders are on the [IGTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html) object.

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.html)
[IGtol::GetLeaderSide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.html)
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.html)
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.html)
[IGtol::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.html)
