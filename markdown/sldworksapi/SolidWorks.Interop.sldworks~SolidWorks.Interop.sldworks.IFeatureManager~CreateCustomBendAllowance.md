---
title: "CreateCustomBendAllowance Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCustomBendAllowance.html"
---

# CreateCustomBendAllowance Method (IFeatureManager)

Creates a custom bend allowance to use when creating a sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCustomBendAllowance() As CustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As CustomBendAllowance

value = instance.CreateCustomBendAllowance()
```

### C#

```csharp
CustomBendAllowance CreateCustomBendAllowance()
```

### C++/CLI

```cpp
CustomBendAllowance^ CreateCustomBendAllowance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) object

## VBA Syntax

See [FeatureManager::CreateCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateCustomBendAllowance.html).

## Examples

[Insert Sheet Metal Hem (VBA)](Insert_Sheet_Metal_Hem_Example_VB.htm)
[Insert Sheet Metal Hem (VB.NET)](Insert_Sheet_Metal_Hem_Example_VBNET.htm)
[Insert Sheet Metal Hem (C#)](Insert_Sheet_Metal_Hem_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[BendsFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html)
[IEdgeFlangeFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~SetCustomBendAllowance.html)
[IFeature::InsertSheetMetalBaseFlange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange.html)
[IHemFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~SetCustomBendAllowance.html)
[IJogFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~SetCustomBendAllowance.html)
[IMiterFlangeFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~SetCustomBendAllowance.html)
[IOneBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.html)
[ISheetMetalFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.html)
[ISketchBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetCustomBendAllowance.html)
[IFeatureManager::InsertSheetMetalHem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
