---
title: "FinishCornerRelief Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FinishCornerRelief"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishCornerRelief.html"
---

# FinishCornerRelief Method (IFeatureManager)

Creates a sheet metal corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function FinishCornerRelief() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.FinishCornerRelief()
```

### C#

```csharp
Feature FinishCornerRelief()
```

### C++/CLI

```cpp
Feature^ FinishCornerRelief();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FinishCornerRelief](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FinishCornerRelief.html).

## Examples

[Create Corner Relief Feature (C#)](Create_Corner_Relief_Feature_Example_CSharp.htm)
[Create Corner Relief Feature (VBA)](Create_Corner_Relief_Feature_Example_VB.htm)
[Create Corner Relief Feature (VB.NET)](Create_Corner_Relief_Feature_Example_VBNET.htm)

## Remarks

Before calling this method, call:

1. [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Mark = 0 and Append = true to select the sheet metal body in which to create a corner relief feature.
2. IModelDocExtension::SelectByID2 with Mark = 4 and Append = true to select two faces that form a bend corner.
3. Call [IFeatureManager::AddCornerReliefCorner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddCornerReliefCorner.html) to add the corner to the corner relief feature.
4. Call [IFeatureManager::AddCornerReliefType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddCornerReliefType.html) to specify the corner relief for the corner.
5. Repeat steps 2 - 4 to add another corner to the corner relief feature.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
