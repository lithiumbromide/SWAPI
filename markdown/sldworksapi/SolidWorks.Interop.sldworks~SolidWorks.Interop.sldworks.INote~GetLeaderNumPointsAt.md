---
title: "GetLeaderNumPointsAt Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetLeaderNumPointsAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderNumPointsAt.html"
---

# GetLeaderNumPointsAt Method (INote)

Gets the number of points in the specified leader of this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLeaderNumPointsAt( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetLeaderNumPointsAt(Index)
```

### C#

```csharp
System.int GetLeaderNumPointsAt(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetLeaderNumPointsAt(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of leader on this note

### Return Value

Number of points in the leader

## VBA Syntax

See [Note::GetLeaderNumPointsAt](ms-its:sldworksapivb6.chm::/sldworks~Note~GetLeaderNumPointsAt.html).

## Remarks

Use [INote::GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderCount.html) to see how many leaders are on the note.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetLeaderAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderAtIndex.html)
[INote::GetLeaderInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderInfo.html)
[INote::SetZeroLengthLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.html)
[INote::HasExtraLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.html)
[INote::IsAttached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
