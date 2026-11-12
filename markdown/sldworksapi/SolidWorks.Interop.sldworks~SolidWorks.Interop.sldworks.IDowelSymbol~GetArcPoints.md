---
title: "GetArcPoints Method (IDowelSymbol)"
project: "SOLIDWORKS API Help"
interface: "IDowelSymbol"
member: "GetArcPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetArcPoints.html"
---

# GetArcPoints Method (IDowelSymbol)

Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcPoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDowelSymbol
Dim value As System.Object

value = instance.GetArcPoints()
```

### C#

```csharp
System.object GetArcPoints()
```

### C++/CLI

```cpp
System.Object^ GetArcPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of start, mid, and end point x and y coordinates

## VBA Syntax

See [DowelSymbol::GetArcPoints](ms-its:sldworksapivb6.chm::/sldworks~DowelSymbol~GetArcPoints.html).

## Remarks

If the arc segment is a complete circle, the start and end points are the same, and the midpoint is at the 180 position.

## See Also

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.html)
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html)
[IDowelSymbol::IGetArcPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetArcPoints.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
