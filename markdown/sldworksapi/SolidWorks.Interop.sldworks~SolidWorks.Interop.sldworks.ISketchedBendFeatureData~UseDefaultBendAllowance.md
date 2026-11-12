---
title: "UseDefaultBendAllowance Property (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "UseDefaultBendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseDefaultBendAllowance.html"
---

# UseDefaultBendAllowance Property (ISketchedBendFeatureData)

Gets or sets whether to use the default bend allowance for this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDefaultBendAllowance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim value As System.Boolean

instance.UseDefaultBendAllowance = value

value = instance.UseDefaultBendAllowance
```

### C#

```csharp
System.bool UseDefaultBendAllowance {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDefaultBendAllowance {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the default bend allowance, false does not

## VBA Syntax

See [SketchedBendFeatureData::UseDefaultBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~UseDefaultBendAllowance.html).

## Examples

See [ISketchedBendFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchedBendFeatureData.html) examples.

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)
[Set Custom Bend Deduction (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)
[ISketchedBendFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetCustomBendAllowance.html)
[ISketchedBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetCustomBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
