---
title: "GetTriangleAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetTriangleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleAtIndex.html"
---

# GetTriangleAtIndex Method (IDisplayData)

Gets the triangle at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTriangleAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetTriangleAtIndex(Index)
```

### C#

```csharp
System.object GetTriangleAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetTriangleAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the desired triangle

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DisplayData::GetTriangleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetTriangleAtIndex.html).

## Remarks

The return value is the following array of doubles:

```vb
[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]
```

where:

| vertexPt1 [3] | First XYZ vertex point |
| --- | --- |
| vertexPt2 [3] | Second XYZ vertex point |
| vertexPt3 [3] | Third XYZ vertex point |
| isFilled | Boolean returned as a double that is True if the triangle is filled, false otherwise |
| lineType | Line type as defined in swLineTypes_e |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTriangleAtIndex.html)
[IDisplayData::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleCount.html)
