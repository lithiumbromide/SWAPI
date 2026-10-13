---
title: "FractionBase Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "FractionBase"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~FractionBase.html"
---

# FractionBase Property (IUserUnit)

Gets the fraction base.

## Syntax

### Visual Basic (Declaration)

```vb
Property FractionBase As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Integer

instance.FractionBase = value

value = instance.FractionBase
```

### C#

```csharp
System.int FractionBase {get; set;}
```

### C++/CLI

```cpp
property System.int FractionBase {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Base as defined in [swFractionDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html)

## VBA Syntax

See [UserUnit::FractionBase](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~FractionBase.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
