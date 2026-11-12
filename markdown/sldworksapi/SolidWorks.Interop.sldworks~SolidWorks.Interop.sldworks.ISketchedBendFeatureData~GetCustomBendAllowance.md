---
title: "GetCustomBendAllowance Method (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (ISketchedBendFeatureData)

Gets the custom bend allowance for this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As CustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim value As CustomBendAllowance

value = instance.GetCustomBendAllowance()
```

### C#

```csharp
CustomBendAllowance GetCustomBendAllowance()
```

### C++/CLI

```cpp
CustomBendAllowance^ GetCustomBendAllowance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [SketchedBendFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~GetCustomBendAllowance.html).

## Examples

See [ISketchedBendFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchedBendFeatureData.html) examples.

## Examples

[Change Bend Radius of Sketched Bend (VBA)](Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm)
[Set Custom Bend Deduction (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)
[ISketchedBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetCustomBendAllowance.html)
[ISketchedBendFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
