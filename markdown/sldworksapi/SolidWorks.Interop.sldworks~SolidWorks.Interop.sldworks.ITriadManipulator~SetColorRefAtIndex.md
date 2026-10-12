---
title: "SetColorRefAtIndex Method (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "SetColorRefAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~SetColorRefAtIndex.html"
---

# SetColorRefAtIndex Method (ITriadManipulator)

Sets the colors of the controls of a triad manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetColorRefAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ColorRef As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator
Dim Index As System.Integer
Dim ColorRef As System.Integer

instance.SetColorRefAtIndex(Index, ColorRef)
```

### C#

```csharp
void SetColorRefAtIndex(
   System.int Index,
   System.int ColorRef
)
```

### C++/CLI

```cpp
void SetColorRefAtIndex(
   System.int Index,
   System.int ColorRef
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Control whose color to set as defined in [swTriadManipulatorControlPoints_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTriadManipulatorControlPoints_e.html)
- `ColorRef`: COLORREF value

## VBA Syntax

See [TriadManipulator::SetColorRefAtIndex](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~SetColorRefAtIndex.html).

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
