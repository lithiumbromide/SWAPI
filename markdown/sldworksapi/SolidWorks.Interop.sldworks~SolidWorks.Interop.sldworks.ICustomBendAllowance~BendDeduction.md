---
title: "BendDeduction Property (ICustomBendAllowance)"
project: "SOLIDWORKS API Help"
interface: "ICustomBendAllowance"
member: "BendDeduction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendDeduction.html"
---

# BendDeduction Property (ICustomBendAllowance)

Gets or sets the value of the bend deduction.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendDeduction As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomBendAllowance
Dim value As System.Double

instance.BendDeduction = value

value = instance.BendDeduction
```

### C#

```csharp
System.double BendDeduction {get; set;}
```

### C++/CLI

```cpp
property System.double BendDeduction {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the bend deduction

## VBA Syntax

See [CustomBendAllowance::BendDeduction](ms-its:sldworksapivb6.chm::/sldworks~CustomBendAllowance~BendDeduction.html).

## Examples

See [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) examples.

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## Remarks

If using this property to set a value for the bend deduction, then the [type of custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~Type.html) is set to this type. However, the last ICustomBendAllowance property called to set a value also re-sets the type of custom bend allowance to its type.

See the ICustomBendAllowance Remarks.

## See Also

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
