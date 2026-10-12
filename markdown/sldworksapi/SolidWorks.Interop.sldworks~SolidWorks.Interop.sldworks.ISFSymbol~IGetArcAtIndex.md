---
title: "IGetArcAtIndex Method (ISFSymbol)"
project: "SOLIDWORKS API Help"
interface: "ISFSymbol"
member: "IGetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArcAtIndex.html"
---

# IGetArcAtIndex Method (ISFSymbol)

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
Dim instance As ISFSymbol
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

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISFSymbol::GetArcCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetArcCount.html) before calling this method to get the number of arcs in this surface finish symbol.

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

| lineType | = Line type as defined in swLineTypes_e enumeration |
| --- | --- |
| startPt [3] | = XYZ arc start point |
| endPt [3] | = XYZ arc end point |
| centerPt [3] | = XYZ arc center point |
| rotationDir | = Value is a boolean returned as a double and represents the rotation direction, where CCW = True and CW = FALS |

## See Also

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.html)
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html)
[ISFSymbol::GetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArcAtIndex.html)
