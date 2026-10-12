---
title: "Tolerance Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "Tolerance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Tolerance.html"
---

# Tolerance Property (ISpring)

Gets or sets the precision of the helical curve.

## Syntax

### Visual Basic (Declaration)

```vb
Property Tolerance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.Tolerance = value

value = instance.Tolerance
```

### C#

```csharp
System.double Tolerance {get; set;}
```

### C++/CLI

```cpp
property System.double Tolerance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance

## VBA Syntax

See [Spring::Tolerance](ms-its:sldworksapivb6.chm::/sldworks~Spring~Tolerance.html).

## Remarks

Tolerance applies to the extension, torsion, and spiral springs only; tolerance does not apply to springs with variable pitches such as compression springs.

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
