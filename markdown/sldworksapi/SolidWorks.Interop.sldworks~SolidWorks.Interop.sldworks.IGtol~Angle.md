---
title: "Angle Property (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~Angle.html"
---

# Angle Property (IGtol)

Gets or sets the rotation angle of this Gtol symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

Rotation angle in radians

## VBA Syntax

See [Gtol::Angle](ms-its:sldworksapivb6.chm::/sldworks~Gtol~Angle.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
