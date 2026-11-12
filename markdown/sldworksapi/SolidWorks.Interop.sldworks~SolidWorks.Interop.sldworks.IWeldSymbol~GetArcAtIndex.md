---
title: "GetArcAtIndex Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "GetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArcAtIndex.html"
---

# GetArcAtIndex Method (IWeldSymbol)

Gets information for the specified arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetArcAtIndex(Index)
```

### C#

```csharp
System.object GetArcAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetArcAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the arc where the index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [WeldSymbol::GetArcAtIndex](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~GetArcAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

| lineType | = line type as defined in swLineTypes_e . |
| --- | --- |
| startPt[3] | = XYZ arc start point. |
| endPt[3] | = XYZ arc end point. |
| centerPt[3] | = XYZ arc center point. |
| rotationDir | = value is a BOOLEAN returned as a double and represents the rotation direction, where CCW = TRUE and CW = FALSE. |

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArcCount.html)
[IWeldSymbol::IGetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArcAtIndex.html)
