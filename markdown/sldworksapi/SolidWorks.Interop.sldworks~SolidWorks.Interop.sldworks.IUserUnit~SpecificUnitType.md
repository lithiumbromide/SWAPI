---
title: "SpecificUnitType Property (IUserUnit)"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: "SpecificUnitType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~SpecificUnitType.html"
---

# SpecificUnitType Property (IUserUnit)

Gets the specific unit type for this user unit.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpecificUnitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
Dim value As System.Integer

instance.SpecificUnitType = value

value = instance.SpecificUnitType
```

### C#

```csharp
System.int SpecificUnitType {get; set;}
```

### C++/CLI

```cpp
property System.int SpecificUnitType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

| If IUserUnit::UnitType is swUserUnitsType_e ... | Then this property is as defined in... |
| --- | --- |
| swLengthUnit | swLengthUnit_e |
| swAngleUnit | swAngleUnit_e |

## VBA Syntax

See [UserUnit::SpecificUnitType](ms-its:sldworksapivb6.chm::/sldworks~UserUnit~SpecificUnitType.html).

## Examples

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) examples.

## See Also

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html)
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
