---
title: "PadZero Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "PadZero"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~PadZero.html"
---

# PadZero Property (IUserUnit)

Gets whether to pad with zeroes.

## Syntax

### Visual Basic (Declaration)

```vb
Property PadZero As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Boolean

instance.PadZero = value

value = instance.PadZero
```

### C#

```csharp
System.bool PadZero {get; set;}
```

### C++/CLI

```cpp
property System.bool PadZero {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to pad with zeroes, false to not

## VBA Syntax

See [UserUnit::PadZero](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~PadZero.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
