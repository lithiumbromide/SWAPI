---
title: "GetTriangleAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetTriangleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTriangleAtIndex.html"
---

# GetTriangleAtIndex Method (INote)

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
Dim instance As INote
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

See [Note::GetTriangleAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetTriangleAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ vertexPt1[3], vertexPt2[3], vertexPt3[3], isFilled, lineType ]

where:

| vertexPt1 [3] | = first XYZ vertex point |
| --- | --- |
| vertexPt2 [3] | = second XYZ vertex point |
| vertexPt3 [3] | = third XYZ vertex point |
| isFilled | = BOOLEAN returned as a double and is True if the triangle is filled, false otherwise |
| lineType | = line type; see swLineTypes_e |

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTriangleCount.html)
[INote::IGetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTriangleAtIndex.html)
