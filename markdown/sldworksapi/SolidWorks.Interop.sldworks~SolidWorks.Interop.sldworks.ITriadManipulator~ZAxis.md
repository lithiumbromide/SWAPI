---
title: "ZAxis Property (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "ZAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~ZAxis.html"
---

# ZAxis Property (ITriadManipulator)

Gets or sets the z axis for this triad manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property ZAxis As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator
Dim value As MathVector

instance.ZAxis = value

value = instance.ZAxis
```

### C#

```csharp
MathVector ZAxis {get; set;}
```

### C++/CLI

```cpp
property MathVector^ ZAxis {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IMathVector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [TriadManipulator::ZAxis](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~ZAxis.html).

## Remarks

To update the position of the manipulator, call [ITriadManipulator::UpdatePosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator~UpdatePosition.html). Moving the triad manipulator to the location set by this property is done by the [handler](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2.html).

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)
[ITriadManipulator::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition.html)
[ITriadManipulator::Origin Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~Origin.html)
[ITriadManipulator::XAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~XAxis.html)
[ITriadManipulator::YAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~YAxis.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
