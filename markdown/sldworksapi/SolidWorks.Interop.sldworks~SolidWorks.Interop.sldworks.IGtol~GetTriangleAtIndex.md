---
title: "GetTriangleAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetTriangleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTriangleAtIndex.html"
---

# GetTriangleAtIndex Method (IGtol)

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
Dim instance As IGtol
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

- `Index`: 0-based index of the piece of text

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Gtol::GetTriangleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetTriangleAtIndex.html).

## Remarks

The return value is the following array of doubles:

```vb
[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]
```

where:

vertexPt1[3] = First XYZ vertex point

vertexPt2[3] = Second XYZ vertex point

vertexPt3[3] = Third XYZ vertex point

isFilled = Boolean returned as a double and is True if the triangle is filled, false if not

lineType = Line type (see [swLineTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html))

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetTriangleCount.html)
[IGtol::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTriangleAtIndex.html)
