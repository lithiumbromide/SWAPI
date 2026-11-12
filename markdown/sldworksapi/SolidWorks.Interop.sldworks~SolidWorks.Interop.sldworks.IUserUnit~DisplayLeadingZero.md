---
title: "DisplayLeadingZero Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "DisplayLeadingZero"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~DisplayLeadingZero.html"
---

# DisplayLeadingZero Property (IUserUnit)

Gets whether to display leading zeroes.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayLeadingZero As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Boolean

instance.DisplayLeadingZero = value

value = instance.DisplayLeadingZero
```

### C#

```csharp
System.bool DisplayLeadingZero {get; set;}
```

### C++/CLI

```cpp
property System.bool DisplayLeadingZero {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display the leading zero, false to not

## VBA Syntax

See [UserUnit::DisplayLeadingZero](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~DisplayLeadingZero.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
