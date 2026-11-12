---
title: "RoundToFraction Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "RoundToFraction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~RoundToFraction.html"
---

# RoundToFraction Property (IUserUnit)

Gets whether to round to a fraction.

## Syntax

### Visual Basic (Declaration)

```vb
Property RoundToFraction As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Boolean

instance.RoundToFraction = value

value = instance.RoundToFraction
```

### C#

```csharp
System.bool RoundToFraction {get; set;}
```

### C++/CLI

```cpp
property System.bool RoundToFraction {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to round, false to not

## VBA Syntax

See [UserUnit::RoundToFraction](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~RoundToFraction.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
