---
title: "GetTriangleAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "GetTriangleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTriangleAtIndex.html"
---

# GetTriangleAtIndex Method (ISFSymbol)

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
Dim instance As ISFSymbol
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

- `Index`: Index of the triangle where the index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [SFSymbol::GetTriangleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~SFSymbol~GetTriangleAtIndex.html).

## Remarks

Call [ISFSymbol::GetTriangleCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetTriangleCount.html) before calling this method to get the number of triangles in this surface finish symbol.

The return value is the following array of doubles :

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

where:

| vertexPt1 [3] | = First XYZ vertex point |
| --- | --- |
| vertexPt2 [3] | = Second XYZ vertex point |
| vertexPt3 [3] | = Third XYZ vertex point |
| isFilled | = BOOLEAN returned as a double; True if triangle is filled, false if not |
| lineType | = Line type as defined in swLineTypes_e . |

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTriangleAtIndex.html)
