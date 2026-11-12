---
title: "EndPoint Property (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "EndPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EndPoint.html"
---

# EndPoint Property (IMagneticLine)

Gets and sets the end point of this magnetic line.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndPoint As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim value As MathPoint

instance.EndPoint = value

value = instance.EndPoint
```

### C#

```csharp
MathPoint EndPoint {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ EndPoint {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [MagneticLine::EndPoint](ms-its:sldworksapivb6.chm::/sldworks~MagneticLine~EndPoint.html).

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagneticLine::StartPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~StartPoint.html)
[IMagneticLine::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Angle.html)
[IMagneticLine::EqualSpacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EqualSpacing.html)
[IMagneticLine::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Length.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
