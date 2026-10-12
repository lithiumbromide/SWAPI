---
title: "IGetArcAtIndex Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "IGetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetArcAtIndex.html"
---

# IGetArcAtIndex Method (IWeldSymbol)

Gets information for the specified arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetArcAtIndex(Index)
```

### C#

```csharp
System.double IGetArcAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetArcAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the arc where the index begins at 0

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

| lineType | = line type as defined in swLineTypes_e . |
| --- | --- |
| startPt[3] | = XYZ arc start point. |
| endPt[3] | = XYZ arc end point. |
| centerPt[3] | = XYZ arc center point. |
| rotationDir | = value is a boolean returned as a double and represents the rotation direction, where CCW = 1.0 and CW = 0.0. |

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArcAtIndex.html)
[IWeldSymbol::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetArcCount.html)
