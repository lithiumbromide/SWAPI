---
title: "UnitType Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "UnitType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~UnitType.html"
---

# UnitType Property (IUserUnit)

Gets the user unit type.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UnitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Integer

value = instance.UnitType
```

### C#

```csharp
System.int UnitType {get;}
```

### C++/CLI

```cpp
property System.int UnitType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

User unit type as defined in [swUserUnitsType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserUnitsType_e.html)

## VBA Syntax

See [UserUnit::UnitType](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~UnitType.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
