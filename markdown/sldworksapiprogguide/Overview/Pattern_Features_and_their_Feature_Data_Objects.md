---
title: "Pattern Features and their Feature Data Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Pattern_Features_and_their_Feature_Data_Objects.htm"
---

# Pattern Features and their Feature Data Objects

#### To create a pattern feature:

1. Open a part (or an assembly for a local pattern).
2. Pre-selection of entities may be supported for some pattern features. Refer to the remarks and examples in the pattern-specific feature data interfaces.

  | To create an instance of... | Call IFeatureManager::CreateDefinition ( swFeatureNameID_e ...) |
  | --- | --- |
  | IChainPatternFeatureData | swFmLocalChainPattern |
  | ICircularPatternFeatureData | swFmCirPattern |
  | ILocalCircularPatternFeatureData | swFmLocalCirPattern |
  | ICurveDrivenPatternFeatureData | swFmCurvePattern |
  | ILocalCurvePatternFeatureData | swFmLocalCurvePattern |
  | IDerivedPatternFeatureData | swFmDerivedLPattern |
  | IDimPatternFeatureData | swFmDimPattern |
  | IFillPatternFeatureData | swFmFillPattern |
  | ILinearPatternFeatureData | swFmLPattern |
  | ILocalLinearPatternFeatureData | swFmLocalLPattern |
  | ISketchPatternFeatureData | swFmSketchPattern |
  | ILocalSketchPatternFeatureData | swFmLocalSketchPattern |
  | ITablePatternFeatureData | swFmTablePattern |
3. Modify properties on the pattern-specific feature data object.
4. Create the pattern-specific feature by calling [IFeatureManager::CreateFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateFeature.html).

**To edit a pattern feature:**

1. Call [IFeature::GetDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetDefinition.html) to get the pattern-specific feature data object.
2. Call AccessSelections on the pattern-specific feature data object.
3. Modify properties on the pattern-specific feature data object.
4. Call [IFeature::ModifyDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~ModifyDefinition.html) if you modified the feature or ReleaseSelectionAccess on the pattern-specific feature data object if you did not modify the feature.
