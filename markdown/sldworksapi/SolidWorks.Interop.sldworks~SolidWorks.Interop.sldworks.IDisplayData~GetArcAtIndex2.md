---
title: "GetArcAtIndex2 Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetArcAtIndex2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArcAtIndex2.html"
---

# GetArcAtIndex2 Method (IDisplayData)

Gets information for the specified arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcAtIndex2( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetArcAtIndex2(Index)
```

### C#

```csharp
System.object GetArcAtIndex2(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetArcAtIndex2(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired arc where the index begins at zero

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DisplayData::GetArcAtIndex2](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetArcAtIndex2.html).

## Remarks

The return value is the following array of doubles :

```vb
[ color, lineType, Unused, Unused, startPt[3], endPt[3], centerPt[3], arcNormal[3], rotationDir ]
where:
```

| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| --- | --- |
| LineType | Line type as defined in swLineTypes_e |
| startPt[3] | XYZ arc start point |
| endPt[3] | XYZ arc end point |
| centerPt[3] | XYZ arc center point |
| arcNormal[3] | XYZ arc normal vector |
| rotationDir | Boolean returned as a double that represents the rotation direction, where CCW = True and CW = false |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::IGetLineAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetLineAtIndex2.html)
[IDisplayData::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetArcCount.html)
