---
title: "IGetTriangleAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "IGetTriangleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetTriangleAtIndex.html"
---

# IGetTriangleAtIndex Method (IDatumTag)

Gets the triangle at the specified index of this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTriangleAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetTriangleAtIndex(Index)
```

### C#

```csharp
System.double IGetTriangleAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetTriangleAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of triangle; index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DatumTag::IGetTriangleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~IGetTriangleAtIndex.html).

## Remarks

The return value is the following array of doubles:

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

where:

| vertexPt1 [3] | First XYZ vertex point |
| --- | --- |
| vertexPt2 [3] | Second XYZ vertex point |
| vertexPt3 [3] | Third XYZ vertex point |
| isFilled | Boolean returned as a double that is True if the triangle is filled, false if it is not |
| lineType | Line type as defined in swLineTypes_e |

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::GetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleAtIndex.html)
[IDatumTag::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetTriangleCount.html)
[IDatumTag::FilledTriangle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~FilledTriangle.html)
