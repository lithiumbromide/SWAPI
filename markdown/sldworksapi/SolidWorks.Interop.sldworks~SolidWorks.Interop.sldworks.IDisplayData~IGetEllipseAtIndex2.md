---
title: "IGetEllipseAtIndex2 Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetEllipseAtIndex2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetEllipseAtIndex2.html"
---

# IGetEllipseAtIndex2 Method (IDisplayData)

Gets information for the specified ellipse.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEllipseAtIndex2( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetEllipseAtIndex2(Index)
```

### C#

```csharp
System.double IGetEllipseAtIndex2(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetEllipseAtIndex2(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired ellipse where the index begins at zero

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of doubles:

```vb
[ color, lineType, Unused, Unused, StartPt[3], EndPt[3], CenterPt[3], MajorPt[3], MinorPt[3], ]
```

where:

| color | COLORREF returned as an integer. Return value could be 0 or -1 for default color. |
| --- | --- |
| LineType | Line type as defined in swLineTypes_e . |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the ellipse start point. |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the ellipse end point. If the ellipse is closed, then this will be the same point as the StartPt. |
| CenterPt[3] | Array of 3 doubles (X,Y,Z) describing the ellipse center point. |
| MajorPt[3] | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and the major axis. |
| MinorPt[3] | Array of 3 doubles (X,Y,Z) describing a point on the ellipse and the minor axis. |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetEllipseAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetEllipseAtIndex2.html)
[IDisplayData::GetEllipseCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetEllipseCount.html)
