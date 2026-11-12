---
title: "IGetArcPoints Method (IDowelSymbol)"
project: "SOLIDWORKS API Help"
interface: "IDowelSymbol"
member: "IGetArcPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetArcPoints.html"
---

# IGetArcPoints Method (IDowelSymbol)

Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArcPoints() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDowelSymbol
Dim value As System.Double

value = instance.IGetArcPoints()
```

### C#

```csharp
System.double IGetArcPoints()
```

### C++/CLI

```cpp
System.double IGetArcPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of size 6 containing start, mid, and end point x and y coordinates

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

If the arc segment is a complete circle, the start and end points are the same, and the midpoint is at the 180 position.

## See Also

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.html)
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html)
[IDowelSymbol::GetArcPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetArcPoints.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
