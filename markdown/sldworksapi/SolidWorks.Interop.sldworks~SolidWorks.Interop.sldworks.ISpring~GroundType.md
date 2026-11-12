---
title: "GroundType Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "GroundType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GroundType.html"
---

# GroundType Property (ISpring)

Gets or sets whether the ends of compression spring are ground to a flat surface or have the same pitch as the coil.

## Syntax

### Visual Basic (Declaration)

```vb
Property GroundType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Integer

instance.GroundType = value

value = instance.GroundType
```

### C#

```csharp
System.int GroundType {get; set;}
```

### C++/CLI

```cpp
property System.int GroundType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 for ends to be ground to a flat surface, 1 for ends to have same pitch as the coil

## VBA Syntax

See [Spring::GroundType](ms-its:sldworksapivb6.chm::/sldworks~Spring~GroundType.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
