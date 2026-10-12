---
title: "GetLeaderAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetLeaderAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderAtIndex.html"
---

# GetLeaderAtIndex Method (INote)

Gets information about the specified leader on this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
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

See [Note::GetLeaderAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetLeaderAtIndex.html).

## Remarks

There can be 0, 1, or 2 lines used with the leader line. In other words, if the note is not attached, then there are 0 lines; otherwise, you can have a straight leaderline (1 line) or a bent leaderline (2 lines). You must infer the number of leader lines based on IsAttached() and HasExtraLeader().

- IsAttached() == false implies no leaderline and no leaderline points (PointCount=0).
- HasExtraLeader() == false implies that this is a straight leaderline and 1 line (PointCount=2)
- HasExtraLeader() == True means that this is a bent leaderline and 2 lines (PointCount=3)

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

Use [INote::GetLeaderCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetLeaderCount.html) to see how many leaders there are on the note.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderInfo.html)
[INote::HasExtraLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.html)
[INote::IGetLeaderAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderAtIndex.html)
[INote::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderInfo.html)
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::HasExtraLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.html)
[INote::IsAttached Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.html)
[INote::GetLeaderNumPointsAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderNumPointsAt.html)
