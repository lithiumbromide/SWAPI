---
title: "SignificantDigits Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "SignificantDigits"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~SignificantDigits.html"
---

# SignificantDigits Property (IUserUnit)

Gets the number of significant digits.

## Syntax

### Visual Basic (Declaration)

```vb
Property SignificantDigits As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Integer

instance.SignificantDigits = value

value = instance.SignificantDigits
```

### C#

```csharp
System.int SignificantDigits {get; set;}
```

### C++/CLI

```cpp
property System.int SignificantDigits {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of significant digits

## VBA Syntax

See [UserUnit::SignificantDigits](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~SignificantDigits.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
