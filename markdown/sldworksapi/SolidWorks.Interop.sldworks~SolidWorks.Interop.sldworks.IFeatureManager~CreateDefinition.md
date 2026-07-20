---
title: "CreateDefinition Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html"
---

# CreateDefinition Method (IFeatureManager)

Creates a feature data object of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDefinition( _
   ByVal Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Integer
Dim value As System.Object

value = instance.CreateDefinition(Type)
```

### C#

```csharp
System.object CreateDefinition(
   System.int Type
)
```

### C++/CLI

```cpp
System.Object^ CreateDefinition(
   System.int Type
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Type`: Feature name ID as defined in[swFeatureNameID_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureNameID_e.html):

- swFmBaseFlange (sheet metal base flange)
- swFmBeltAndChain (belt/chain)
- swFmBoundingBox (bounding box)
- swFmCirPattern (circular pattern)
- swFmCornerRelief (sheet metal corner relief)
- swFmCurvePattern (curve-driven pattern)
- swFmDerivedLPattern (derived-driven pattern)
- swFmDimPattern (variable/dimension pattern)
- swFmEdgeFlange (sheet metal edge flange)
- swFmFillet (constant radius, face, full round fillet/chamfer)
- swFmFillPattern (fill pattern)
- swFmFormToolInstance (library form tool)
- swFmGroundPlane (ground plane)
- swFmLibraryFeature (library)
- swFmLocalChainPattern (chain component pattern)
- swFmLocalCirPattern (circular component pattern)
- swFmLocalCurvePattern (curve-driven component pattern)
- swFmLocalLPattern (linear component pattern)
- swFmLocalSketchPattern (sketch-driven component pattern)
- swFmLPattern (linear pattern)
- swFmMateController (mate controller)
- swFmMirrorComponent (mirror components)
- swFmNormalCut (sheet metal normal cut)
- swFmRefCurve (projection curve)
- swFmRefSurface (surface sweep)
- swFmSketchBend (sheet metal sketched bend)
- swFmSketchPattern (sketch-driven pattern)
- swFmSMGusset (sheet metal gusset)
- swFmSolidToSheetMetal (convert solid to sheet metal)
- swFmSweep (boss sweep)
- swFmSweepCut (cut sweep)
- swFmSweepThread (sweep thread)
- swFmSweptFlange (sheet metal swept flange)
- swFmTabAndSlot (tab and slot)
- swFmTablePattern (table pattern)

### Return Value

[thread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)

,

[sweep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)

,

[library](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)

,

[library form tool](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

,

[tab and slot](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.html)

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

,

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

, or pattern-specific feature data object (see

Remarks

); Nothing or null otherwise

## VBA Syntax

See

[FeatureManager::CreateDefinition](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateDefinition.html)

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

This method initializes the feature data objects with default data for pattern, sweep, bounding box, ground plane, mirror components, projection curve, sheet metal normal cut, sheet metal swept flange, sheet metal gusset, sheet metal edge flange, tab/slot, library form tool, and belt/chain features.

For sheet metal base flange, sheet metal corner relief, convert solid to sheet metal, library, simple fillet, and thread features, you must initialize feature data objects using specific initialize methods.

For mate controller features, you can either pre-select mates before calling this method or initialize the feature data object returned by this method with default values.

See the**See Also**section.

For additional information, see:

- [Library Features and LibraryFeatureData Objects](sldworksAPIProgGuide.chm::/OVERVIEW/Library_Features_and_LibraryFeatureData_Objects.htm)
- [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm)
- [Sweep Features and SweepFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Sweep_Features_and_SweepFeatureData_Objects.htm)
- [Thread Features and ThreadFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Thread_Features_and_ThreadFeatureData_Objects.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)

[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

[IFeature::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html)

[IFeature::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetDefinition.html)

[IFeatureManager::CreateFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html)

[ILibraryFeatureData::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~Initialize.html)

[IThreadFeatureData::InitializeThreadData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~InitializeThreadData.html)

[ISimpleFilletFeatureData2::Initialize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.html)

[IBaseFlangeFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html)

[ICornerReliefFeatureData::Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~Initialize.html)

[IMateControllerFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize.html)

[IConvertSolidFeatureData::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~Initialize.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
