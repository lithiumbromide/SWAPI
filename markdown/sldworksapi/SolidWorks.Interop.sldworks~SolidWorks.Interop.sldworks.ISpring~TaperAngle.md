---
title: "TaperAngle Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "TaperAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~TaperAngle.html"
---

# TaperAngle Property (ISpring)

Gets or sets the angle by which to taper a compression spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property TaperAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.TaperAngle = value

value = instance.TaperAngle
```

### C#

```csharp
System.double TaperAngle {get; set;}
```

### C++/CLI

```cpp
property System.double TaperAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle by which to taper the spring

## VBA Syntax

See [Spring::TaperAngle](ms-its:sldworksapivb6.chm::/sldworks~Spring~TaperAngle.html).

## Remarks

Use [ISpring::TaperOutward](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring~TaperOutward.html) to set the direction of the taper outward or inward.

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
