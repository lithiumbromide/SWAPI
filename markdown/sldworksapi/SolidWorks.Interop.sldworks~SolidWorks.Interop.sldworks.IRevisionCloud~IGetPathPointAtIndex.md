---
title: "IGetPathPointAtIndex Method (IRevisionCloud)"
project: "SOLIDWORKS API Help"
interface: "IRevisionCloud"
member: "IGetPathPointAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~IGetPathPointAtIndex.html"
---

# IGetPathPointAtIndex Method (IRevisionCloud)

Gets the coordinates of a point with the specified index on the path of this revision cloud annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPathPointAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionCloud
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetPathPointAtIndex(Index)
```

### C#

```csharp
System.double IGetPathPointAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetPathPointAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of a point on the path of this revision cloud annotation (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles of x, y, and z coordinates of a point on the path of this revision cloud annotation
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To get the range of values for Index, call [IRevisionCloud::GetPathPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~GetPathPointCount.html) to get the total number of points on the path of this revision cloud annotation.

## See Also

[IRevisionCloud Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud.html)
[IRevisionCloud Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html)
[IRevisionCloud::GetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~GetPathPointAtIndex.html)
[IRevisionCloud::SetPathPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud~SetPathPointAtIndex.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
