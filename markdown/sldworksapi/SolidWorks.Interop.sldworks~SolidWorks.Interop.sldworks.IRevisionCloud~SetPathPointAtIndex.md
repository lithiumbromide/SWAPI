---
title: "SetPathPointAtIndex Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "SetPathPointAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.html"
---

# SetPathPointAtIndex Method (IRevisionCloud)

Sets the specified coordinates of a point at the specified index on the path of this revision cloud annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPathPointAtIndex( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim Index As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SetPathPointAtIndex(Index, X, Y, Z)
```

### C#

```csharp
System.bool SetPathPointAtIndex(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetPathPointAtIndex(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of an existing point on the path of this revision cloud annotation; -1 if creating a new point (see **Remarks**)
- `X`: x coordinate of the point
- `Y`: y coordinate of the point
- `Z`: z coordinate of the point

### Return Value

True if successful, false if not

## VBA Syntax

See [RevisionCloud::SetPathPointAtIndex](ms-its:sldworksapivb6.chm::/sldworks~RevisionCloud~SetPathPointAtIndex.html).

## Examples

See [IRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud.html) examples.

## Remarks

To get the range of values for Index, call [IRevisionCloud::GetPathPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~GetPathPointCount.html) to get the total number of points on the path of this revision cloud annotation.

You can create a new path point by calling this method, setting Index to -1. You can create new path points any time after [IDrawingDoc::InsertRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertRevisionCloud.html) or [IDrawingDoc::IInsertRevisionCloud](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IInsertRevisionCloud.html) is called. You cannot create new path points after [IRevisionCloud::Finalize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~Finalize.html) is called.

You can call this method at any time to change the position of existing path points.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)
[IRevisionCloud::GetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointAtIndex.html)
[IRevisionCloud::IGetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetPathPointAtIndex.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
