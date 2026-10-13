---
title: "TaperOutward Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "TaperOutward"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~TaperOutward.html"
---

# TaperOutward Property (ISpring)

Gets or sets the direction by which to taper the helix of a compression spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property TaperOutward As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Boolean

instance.TaperOutward = value

value = instance.TaperOutward
```

### C#

```csharp
System.bool TaperOutward {get; set;}
```

### C++/CLI

```cpp
property System.bool TaperOutward {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to taper the helix outward, false to tape inward

## VBA Syntax

See [Spring::TaperOutward](ms-its:sldworksapivb6.chm::/sldworks~Spring~TaperOutward.html).

## Remarks

Use [ISpring::TaperAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring~TaperAngle.html) to set the angle by which to taper a spring.

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
