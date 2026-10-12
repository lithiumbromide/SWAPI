---
title: "Sweep Features and SweepFeatureData Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Sweep_Features_and_SweepFeatureData_Objects.htm"
---

# Sweep Features and SweepFeatureData Objects

#### To create a Sweep feature:

- See the [ISweepFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData.html) examples.
- Open a part in SOLIDWORKS and create a profile and a path along which to sweep the profile. Create guide curves, if using a sketch profile.
- In a macro:

  - Access the part.
  - Call [IModelDocExtension::SelectByRay](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelDocExtension~SelectByRay.html) to select the:

    1. **Profile**:

      - If a sketch profile, use Mark = 1 to select a face, edge, or curve. For a swept-boss feature, the sketch profile must be closed. For a swept-surface feature, the sketch profile is open or closed.
      - If a circular profile, use Mark = 4 to select a sketch line, edge or curve. The circular profile is open or closed.
      - If a solid profile, use Mark = 1 to select the tool body to use to make the cut and use Mark = 2048 to select the solid body to cut. Solid profiles are used only in swept-cut features.
    2. **Sweep path** using Mark = 4:

      - Select a set of sketched curves contained in one sketch, a curve, or a set of model edges.
      - The sweep path is open or closed.
      - The starting point of the sweep path must lie on the plane of the profile for a 1-directional sweep. If the sweep path extends to both sides of the profile, you can create a bidirectional sweep.
      - Sweep paths are not used with circular profiles.
    3. **Guide curves** using Mark = 2:

      - Guide curves are used only with sketch profiles.
      - A guide curve must be coincident with the sketch profile or with a point on the profile sketch.
      - Guide curves are not used in bidirectional sweeps.
    4. **Direction vector** using Mark = 128:

      - Select a plane, face, line, axis, edge, cylinder, or a pair of vertices that define the direction.
  - To create a SweepFeatureData object and initialize it with default properties for a:
- If you specified a direction vector in step 3.2.4 above, then before creating the sweep feature you must:

  - Set [ISweepFeatureData::PathAlignmentType](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~PathAlignmentType.html) to [swTangencyType_e](swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e.html).swTangencyDirectionVector.
  - Set [ISweepFeatureData::TwistControlType](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~TwistControlType.html) to [swTwistControlType_e](swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlFollowPath.
- Before creating a thin-walled swept-cut or swept-boss feature, you must:

  - Set [ISweepFeatureData::ThinFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~ThinFeature.html) to true.
  - Set [ISweepFeatureData::ThinWallType](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~ThinWallType.html).
  - Call [ISweepFeatureData::SetWallThickness](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~SetWallThickness.html).
- Modify other ISweepFeatureData properties that apply to the selected profile. For example for a sketch profile, if the sweep path extends to both sides of the profile, you can make the sweep bidirectional by setting [ISweepFeatureData::Direction](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~Direction.html). See the SOLIDWORKS help and [ISweepFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData.html) for more information about sweep feature properties.
- Create the sweep feature by calling [IFeatureManager::CreateFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~CreateFeature.html)(SweepFeatureData object).

#### To edit the Sweep feature:

1. Call [IFeature::GetDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetDefinition.html) to access the SweepFeatureData object.
2. Call [ISweepFeatureData::AccessSelections](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~AccessSelections.html).
3. Modify ISweepFeatureData object properties. Note that you cannot create a thin-walled sweep feature at this point.
4. Call [IFeature::ModifyDefinition](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~ModifyDefinition.html), if you modified the feature, or [ISweepFeatureData::ReleaseSelectionAccess](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISweepFeatureData~ReleaseSelectionAccess.html), if you did not modify the feature.
