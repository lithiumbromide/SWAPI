---
title: "Origin Property (ITriadManipulator)"
project: "SOLIDWORKS API Help"
interface: "ITriadManipulator"
member: "Origin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~Origin.html"
---

# Origin Property (ITriadManipulator)

Gets or sets the origin for this triad manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property Origin As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ITriadManipulator
Dim value As MathPoint

instance.Origin = value

value = instance.Origin
```

### C#

```csharp
MathPoint Origin {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ Origin {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [TriadManipulator::Origin](ms-its:sldworksapivb6.chm::/sldworks~TriadManipulator~Origin.html).

## Examples

See the [ITriadManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html) examples.

## Remarks

To update the position of the manipulator, call [ITriadManipulator::UpdatePosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator~UpdatePosition.html). Moving the triad manipulator to the location set by this property is done by the [handler](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2.html).

## See Also

[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[ITriadManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html)
[ITriadManipulator::UpdatePosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~UpdatePosition.html)
[ITriadManipulator::XAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~XAxis.html)
[ITriadManipulator::YAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~YAxis.html)
[ITriadManipulator::ZAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator~ZAxis.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
