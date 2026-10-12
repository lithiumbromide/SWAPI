---
title: "LockMagneticMate Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "LockMagneticMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~LockMagneticMate.html"
---

# LockMagneticMate Property (IMate2)

Gets or sets whether to lock this magnetic mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property LockMagneticMate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

instance.LockMagneticMate = value

value = instance.LockMagneticMate
```

### C#

```csharp
System.bool LockMagneticMate {get; set;}
```

### C++/CLI

```cpp
property System.bool LockMagneticMate {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to lock, false to not

## VBA Syntax

See [Mate2::LockMagneticMate](ms-its:sldworksapivb6.chm::/sldworks~Mate2~LockMagneticMate.html).

## Remarks

This property is valid only if [IMate2::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.html) is set to [swMateType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html).swMateMAGNETIC.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
