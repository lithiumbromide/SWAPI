---
title: "Type Property (ICustomBendAllowance)"
project: "SOLIDWORKS API Help"
interface: "ICustomBendAllowance"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~Type.html"
---

# Type Property (ICustomBendAllowance)

Gets or sets the bend allowance type.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICustomBendAllowance
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend allowance type as defined in [swBendAllowanceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendAllowanceTypes_e.html)

## VBA Syntax

See [CustomBendAllowance::Type](ms-its:sldworksapivb6.chm::/sldworks~CustomBendAllowance~Type.html).

## Examples

See the [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) examples.

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Examples

[Change Bend Radius of Sketch Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)
[Set Custom Bend Deduction (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)
[Set Custom Bend Deduction (VB.NET)](Set_Custom_Bend_Deduction_Example_VBNET.htm)
[Set Custom Bend Deduction (C#)](Set_Custom_Bend_Deduction_Example_CSharp.htm)

## Remarks

After setting [ICustomBendAllowance::BendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~BendAllowance.html), [ICustomBendAllowance::BendDeduction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~BendDeduction.html), [ICustomBendAllowance::BendTableFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendTableFile.html), [ICustomBendAllowance::BendCalculationTableFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance~BendCalculationTableFile.html), and [ICustomBendAllowance::KFactor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance~KFactor.html) use this property to set the value for the type. If you do not set this property last, the ICustomBendAllowance property set last automatically overrides any previously set custom bend allowance type.

See the ICustomBendAllowance Remarks.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICustomBendAllowance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.html)
[ICustomBendAllowance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
