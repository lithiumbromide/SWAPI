---
title: "GetPathPointAtIndex Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "GetPathPointAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointAtIndex.html"
---

# GetPathPointAtIndex Method (IRevisionCloud)

Gets the coordinates of a point with the specified index on the path of this revision cloud annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathPointAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetPathPointAtIndex(Index)
```

### C#

```csharp
System.object GetPathPointAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetPathPointAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of a point on the path of this revision cloud annotation (see **Remarks**)

### Return Value

Array of doubles of the x, y, and z coordinates of a point on the path of this revision cloud annotation

## VBA Syntax

See [RevisionCloud::GetPathPointAtIndex](ms-its:sldworksapivb6.chm::/sldworks~RevisionCloud~GetPathPointAtIndex.html).

## Remarks

To get the range of values for Index, call [IRevisionCloud::GetPathPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~GetPathPointCount.html) to get the total number of points on the path of this revision cloud annotation.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)
[IRevisionCloud::IGetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetPathPointAtIndex.html)
[IRevisionCloud::SetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
