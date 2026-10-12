---
title: "FilletXpertChange Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FilletXpertChange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.html"
---

# FilletXpertChange Method (IFeatureManager)

Changes the parameters on the selected filleted faces, regardless of whether the filleted faces were created manually or with FilletXpert, provided that FilletXpert can process them.

## Syntax

### Visual Basic (Declaration)

```vb
Function FilletXpertChange( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim value As Feature

value = instance.FilletXpertChange(Options, R1, Ftyp, OverflowType)
```

### C#

```csharp
Feature FilletXpertChange(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType
)
```

### C++/CLI

```cpp
Feature^ FilletXpertChange(
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Feature fillet option as defined in [swFeatureFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html)
- `R1`: Radius for uniform radius edge fillet
- `Ftyp`: Type of fillet as defined in [swFeatureFilletType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html)
- `OverflowType`: Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FilletXpertChange](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FilletXpertChange.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.html)
[IFeatureManager::FilletXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
