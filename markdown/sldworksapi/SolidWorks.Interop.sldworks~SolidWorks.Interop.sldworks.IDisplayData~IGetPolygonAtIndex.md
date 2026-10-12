---
title: "IGetPolygonAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetPolygonAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolygonAtIndex.html"
---

# IGetPolygonAtIndex Method (IDisplayData)

Gets information for the specified polygon.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPolygonAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetPolygonAtIndex(Index)
```

### C#

```csharp
System.double IGetPolygonAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetPolygonAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired polygon where the index begins at zero

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Format of return values is an array of doubles with the format:

```vb
[ Color, LineType, Unused, Unused, NumPolyPoints, [x,y,z] ]
```

where:

| Color | Polygon color |
| --- | --- |
| LineType | Line type as defined in swLineTypes_e . You can use this index value with IDrawingDoc::GetLineFontInfo2 and IDrawingDoc::GetLineFontName2 |
| NumPolyPoints | Number of XYZ points found in the [x,y,z] return value |
| [x,y,z] | Array of NumPolyPoints points used to describe the polygon |

Use [IDisplayData::GetPolygonSizeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.html) to determine the number of elements in this array.

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetPolygonAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonAtIndex.html)
[IDisplayData::GetPolygonCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonCount.html)
[IDisplayData::GetPolygonSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.html)
