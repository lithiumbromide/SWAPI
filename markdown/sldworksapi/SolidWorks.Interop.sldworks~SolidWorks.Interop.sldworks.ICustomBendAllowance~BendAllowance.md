---
title: "BendAllowance Property (ICustomBendAllowance)"
project: "SOLIDWORKS API Help"
interface: "ICustomBendAllowance"
member: "BendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendAllowance.html"
---

# BendAllowance Property (ICustomBendAllowance)

Gets or sets the value of the bend allowance.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAllowance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomBendAllowance
Dim value As System.Double

instance.BendAllowance = value

value = instance.BendAllowance
```

### C#

```csharp
System.double BendAllowance {get; set;}
```

### C++/CLI

```cpp
property System.double BendAllowance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value (m) of the bend allowance

## VBA Syntax

See [CustomBendAllowance::BendAllowance](ms-its:sldworksapivb6.chm::/sldworks~CustomBendAllowance~BendAllowance.html).

## Examples

See the [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) examples.

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)

## Remarks

If using this property to set a value for the bend allowance, then the [type of custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~Type.html) is set to this type. However, the last ICustomBendAllowance property set also re-sets the type of bend allowance to its type.

See the ICustomBendAllowance Remarks.

## See Also

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
