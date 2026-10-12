---
title: "InsertWeldmentTrimFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertWeldmentTrimFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature.html"
---

# InsertWeldmentTrimFeature Method (IFeatureManager)

Inserts a weldment trim feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWeldmentTrimFeature( _
   ByVal EndCond As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim EndCond As System.Integer
Dim value As Feature

value = instance.InsertWeldmentTrimFeature(EndCond)
```

### C#

```csharp
Feature InsertWeldmentTrimFeature(
   System.int EndCond
)
```

### C++/CLI

```cpp
Feature^ InsertWeldmentTrimFeature(
   System.int EndCond
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EndCond`: End condition as defined by [swSolidworksWeldmentEndCondOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertWeldmentTrimFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertWeldmentTrimFeature.html).

## Remarks

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and specify the following marks to select the body, or bodies, to trim and the trimming boundaries:

- 1 = Body or bodies to trim
- 2 = Trimming boundaries (body or face)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IFeatureManager::InsertWeldmentTrimFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWeldmentTrimFeature2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
