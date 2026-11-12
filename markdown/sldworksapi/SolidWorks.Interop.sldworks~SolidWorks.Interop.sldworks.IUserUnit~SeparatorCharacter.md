---
title: "SeparatorCharacter Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "SeparatorCharacter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~SeparatorCharacter.html"
---

# SeparatorCharacter Property (IUserUnit)

Gets the decimal separator character.

## Syntax

### Visual Basic (Declaration)

```vb
Property SeparatorCharacter As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.String

instance.SeparatorCharacter = value

value = instance.SeparatorCharacter
```

### C#

```csharp
System.string SeparatorCharacter {get; set;}
```

### C++/CLI

```cpp
property System.String^ SeparatorCharacter {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Character passed as a string to represent the decimal separator

## VBA Syntax

See [UserUnit::SeparatorCharacter](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~SeparatorCharacter.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
