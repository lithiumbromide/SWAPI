---
title: "IGetLeaderInfo Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetLeaderInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderInfo.html"
---

# IGetLeaderInfo Method (INote)

Gets information describing the layout of the note leader lines.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLeaderInfo( _
   ByRef PointCount As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim PointCount As System.Integer
Dim value As System.Double

value = instance.IGetLeaderInfo(PointCount)
```

### C#

```csharp
System.double IGetLeaderInfo(
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.double IGetLeaderInfo(
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointCount`: Number of points

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

There can be 0, 1, or 2 lines used with the leader line. If the note is not attached, then there are 0 lines; otherwise, you have a straight leaderline (1 line) or a bent leaderline (2 lines). You must infer the number of leader lines based on IsAttached() and HasExtraLeader().

- IsAttached() == false implies no leaderline and no leaderline points (PointCount=0).
- HasExtraLeader() == false implies a straight leaderline and1 line (PointCount=2)
- HasExtraLeader() == True implies a bent leaderline and 2 lines (PointCount=3)

Format of return information is the following array of doubles:

- return value[0] = x coordinate of first leader point
- return value[1] = y coordinate of first leader point
- return value[2] = z coordinate of first leader point
- return value[3] = x coordinate of second leader point
- return value[4] = y coordinate of second leader point
- return value[5] = z coordinate of second leader point
- return value[6] = x coordinate of third leader point
- return value[7] = y coordinate of third leader point
- return value[8] = z coordinate of third leader point

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderCount.html)
[INote::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderInfo.html)
[INote::GetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderAtIndex.html)
[INote::HasExtraLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.html)
[INote::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderInfo.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::IsAttached Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.html)
