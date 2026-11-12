---
title: "Thread Features and ThreadFeatureData Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Thread_Features_and_ThreadFeatureData_Objects.htm"
---

# Thread Features and ThreadFeatureData Objects

#### To create a Thread feature:

1. See the [IThreadFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData.html) examples.
2. Ensure that **Tools > Options > System Options > File Location > Thread Options > Folder** contains thread profiles (***.sldlfp**).
3. Open a part document with a Hole Wizard hole, Advanced Hole, or Extruded Cut.
4. Call [IFeatureManager::CreateDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateDefinition.html)([swFeatureNameID_e](swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureNameID_e.html).swFmSweepThread) to create a new [ThreadFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData.html) object.
5. Initialize the thread feature data object with default property settings using [IThreadFeatureData::InitializeThreadData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData~InitializeThreadData.html).
6. Select thread feature reference entities using [IModelDocExtension::SelectByRay](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~SelectByRay.html):

  - Edge of cylinder where the thread begins with Mark = 1.
  - Up To Selection end condition reference with Mark = 1.
  - (Optional) Starting location of the thread helix with Mark = 2, (only if step 1 does not select a planar circular edge):

    - [vertex](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IVertex.html)
    - [reference point](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IRefPoint.html)
    - [edge](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IEdge.html)
    - [reference axis](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IRefAxis.html)
    - [reference plane](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IRefPlane.html)
    - [planar surface](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISurface.html)
7. Set [IThreadFeatureData::Edge](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData~Edge.html) with the selection from step 6.1.
8. Call [IThreadFeatureData::SetEndConditionReference](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData~SetEndConditionReference.html) with Value set to the selection from step 6.2.
9. Set [IThreadFeatureData::StartEntity](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData~StartEntity.html) with the selection from step 6.3.
10. Modify other property settings in the ThreadFeatureData object.
11. Create the thread feature by calling [IFeatureManager::CreateFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateFeature.html).

**To edit a Thread feature:**

1. Call [IFeature::GetDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetDefinition.html).
2. Call [IThreadFeatureData::AccessSelections](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData~AccessSelections.html).
3. Modify property settings in the ThreadFeatureData object.
4. Call [IFeature::ModifyDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~ModifyDefinition.html) if you modified the feature or [IThreadFeatureData::ReleaseSelectionAccess](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IThreadFeatureData~ReleaseSelectionAccess.html) if you did not modify the feature.
