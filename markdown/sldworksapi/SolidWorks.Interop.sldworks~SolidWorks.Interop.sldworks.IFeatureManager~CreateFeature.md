---
title: "CreateFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html"
---

# CreateFeature Method (IFeatureManager)

Creates the specified feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeature( _
   ByVal FeatureData As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FeatureData As System.Object
Dim value As Feature

value = instance.CreateFeature(FeatureData)
```

### C#

```csharp
Feature CreateFeature(
   System.object FeatureData
)
```

### C++/CLI

```cpp
Feature^ CreateFeature(
   System.Object^ FeatureData
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `FeatureData`: [thread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)

,

[sweep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)

,

[library](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)

,

[library form tool](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

(see

Remarks

),

[tab/slot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.html)

,

[bounding box](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)

,

[ground plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html)

,

[mirror components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)

,

[projection curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)

,

[sheet metal normal cut](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)

,

[sheet metal swept flange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)

,

[sheet metal gusset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)

,

[sheet metal edge flange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)

,

[convert solid to sheet metal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

(see

Remarks

),

[simple fillet/chamfer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)

,

[belt/chain](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)

,

[sheet metal base flange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)

,

[sheet metal corner relief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)

,

[sheet metal sketched bend](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)

,

[mate controller](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)

, or a pattern-specific feature data object (see

Remarks

)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See

[FeatureManager::CreateFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateFeature.html)

.

## Examples

See examples for:

[IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)

[IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)

[ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)

[IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)

[IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)

[IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)

[IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.html)

[ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)

[ISketchedBendFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.html)

[ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)

[ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)

[ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.html)

## Examples

[Create a Thread Feature (VBA)](Create_a_Thread_Feature_Example_VB.htm)

[Create a Thread Feature (VB.NET)](Create_a_Thread_Feature_Example_VBNET.htm)

[Create a Thread Feature (C#)](Create_a_Thread_Feature_Example_CSharp.htm)

## Remarks

Before calling this method to create ConvertSolid and Library form tool features, ensure that the Sheet Metal tab is visible on the CommandManager toolbar.

Use:

- [IFeature::GetErrorCode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetErrorCode2.html)

  to get any errors that occurred during the creation of the feature.
- [IFeatureManager::GetCreateFeatureErrors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCreateFeatureErrors.html)

  to get any errors that occurred during the creation of a Mate Controller feature.

For additional information, see:

- [Library Features and LibraryFeatureData Objects](sldworksAPIProgGuide.chm::/OVERVIEW/Library_Features_and_LibraryFeatureData_Objects.htm)
- ms-its:sldworksapiprogguide.chm:://Overview/Pattern_Features_and_their_Feature_Data_Objects.htm

  [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm)
- [Sweep Features and SweepFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Sweep_Features_and_SweepFeatureData_Objects.htm)
- [Thread Features and ThreadFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Thread_Features_and_ThreadFeatureData_Objects.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)

[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

[IFeature::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)

[IFeatureManager::CreateDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html)

[ILibraryFeatureData::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize.html)

[IThreadFeatureData::InitializeThreadData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~InitializeThreadData.html)

[ISimpleFilletFeatureData2::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.html)

[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html)

[ICornerReliefFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~Initialize.html)

[IMateControllerFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize.html)

[IConvertSolidFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~Initialize.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
