---
title: "StartPoint Property (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "StartPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~StartPoint.html"
---

# StartPoint Property (IMagneticLine)

Gets and sets the start point of this magnetic line.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartPoint As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim value As MathPoint

instance.StartPoint = value

value = instance.StartPoint
```

### C#

```csharp
MathPoint StartPoint {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ StartPoint {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [MagneticLine::StartPoint](ms-its:sldworksapivb6.chm::/sldworks~MagneticLine~StartPoint.html).

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagneticLine::EndPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EndPoint.html)
[IMagneticLine::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Angle.html)
[IMagneticLine::EqualSpacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EqualSpacing.html)
[IMagneticLine::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Length.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
