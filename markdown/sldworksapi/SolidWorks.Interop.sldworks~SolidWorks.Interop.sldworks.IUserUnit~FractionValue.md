---
title: "FractionValue Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "FractionValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~FractionValue.html"
---

# FractionValue Property (IUserUnit)

Gets the denominator value of the fraction.

## Syntax

### Visual Basic (Declaration)

```vb
Property FractionValue As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Integer

instance.FractionValue = value

value = instance.FractionValue
```

### C#

```csharp
System.int FractionValue {get; set;}
```

### C++/CLI

```cpp
property System.int FractionValue {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fraction denominator value; valid only if [IUserUnit::FractionBase](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~FractionBase.html) is [swFractionDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html).swFRACTION

## VBA Syntax

See [UserUnit::FractionValue](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~FractionValue.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
