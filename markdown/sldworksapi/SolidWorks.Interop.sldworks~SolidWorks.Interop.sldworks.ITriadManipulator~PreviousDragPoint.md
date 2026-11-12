---
title: "PreviousDragPoint Property (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "PreviousDragPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~PreviousDragPoint.html"
---

# PreviousDragPoint Property (ITriadManipulator)

Gets the previous drag position of the triad manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PreviousDragPoint As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator
Dim value As MathPoint

value = instance.PreviousDragPoint
```

### C#

```csharp
MathPoint PreviousDragPoint {get;}
```

### C++/CLI

```cpp
property MathPoint^ PreviousDragPoint {
   MathPoint^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [TriadManipulator::PreviousDragPoint](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~PreviousDragPoint.html).

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
