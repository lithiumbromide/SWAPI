---
title: "Angle Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Angle.html"
---

# Angle Property (IView)

Gets or sets the rotation angle of the view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Rotation angle in radians of the view

## VBA Syntax

See [View::Angle](ms-its:sldworksapivb6.chm::/sldworks~View~Angle.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
