---
title: "SetCustomBendAllowance Method (ISketchedBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchedBendFeatureData"
member: "SetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetCustomBendAllowance.html"
---

# SetCustomBendAllowance Method (ISketchedBendFeatureData)

Sets the custom bend allowance for this sketched bend.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCustomBendAllowance( _
   ByVal PBendData As CustomBendAllowance _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchedBendFeatureData
Dim PBendData As CustomBendAllowance

instance.SetCustomBendAllowance(PBendData)
```

### C#

```csharp
void SetCustomBendAllowance(
   CustomBendAllowance PBendData
)
```

### C++/CLI

```cpp
void SetCustomBendAllowance(
   CustomBendAllowance^ PBendData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PBendData`: [Custom bend allowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html)

## VBA Syntax

See [SketchedBendFeatureData::SetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~SketchedBendFeatureData~SetCustomBendAllowance.html).

## Examples

[Set Custom Bend Deduction (VBA)](Set_Custom_Bend_Deduction_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html)
[ISketchedBendFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~GetCustomBendAllowance.html)
[ISketchedBendFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
