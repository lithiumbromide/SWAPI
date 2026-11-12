---
title: "EqualSpacing Property (IMagneticLine)"
project: "SOLIDWORKS API Help"
interface: "IMagneticLine"
member: "EqualSpacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EqualSpacing.html"
---

# EqualSpacing Property (IMagneticLine)

Gets and sets whether to equally space the notes on this magnetic line.

## Syntax

### Visual Basic (Declaration)

```vb
Property EqualSpacing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMagneticLine
Dim value As System.Boolean

instance.EqualSpacing = value

value = instance.EqualSpacing
```

### C#

```csharp
System.bool EqualSpacing {get; set;}
```

### C++/CLI

```cpp
property System.bool EqualSpacing {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to equally space the notes, false to drag the notes to any location on the magnetic line (see **Remarks**)

## VBA Syntax

See [MagneticLine::EqualSpacing](ms-its:sldworksapivb6.chm::/sldworks~MagneticLine~EqualSpacing.html).

## Examples

[Insert Magnetic Line (VBA)](Insert_Magnetic_Line_Example_VB.htm)
[Insert Magnetic Line (VB.NET)](Insert_Magnetic_Line_Example_VBNET.htm)
[Insert Magnetic Line (C#)](Insert_Magnetic_Line_Example_CSharp.htm)

## Remarks

If this property is set to true, then [IMagneticLine::AddNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMagneticLine~AddNote.html) ignores any Position parameter value.

## See Also

[IMagneticLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine.html)
[IMagneticLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html)
[IMagneticLine::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Angle.html)
[IMagneticLine::EndPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~EndPoint.html)
[IMagneticLine::StartPoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~StartPoint.html)
[IMagneticLine::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine~Length.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
