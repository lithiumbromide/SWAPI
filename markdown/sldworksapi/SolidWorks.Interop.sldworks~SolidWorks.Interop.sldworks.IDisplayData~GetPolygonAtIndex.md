---
title: "GetPolygonAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetPolygonAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonAtIndex.html"
---

# GetPolygonAtIndex Method (IDisplayData)

Gets information for the specified polygon.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPolygonAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetPolygonAtIndex(Index)
```

### C#

```csharp
System.object GetPolygonAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetPolygonAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired polygon where the index begins at zero

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DisplayData::GetPolygonAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetPolygonAtIndex.html).

## Examples

[Get Weld Bead Symbol Data (VBA)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VB.htm)
[Get Weld Bead Symbol Data (VB.NET)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VBNET.htm)
[Get Weld Bead Symbol Data (C#)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_CSharp.htm)

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

Use [IDisplayData::GetPolygonSizeAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.html) to determine the number of elements returned in this array.

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetPolygonCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonCount.html)
[IDisplayData::IGetPolygonAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolygonAtIndex.html)
[IDisplayData::GetPolygonSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.html)
