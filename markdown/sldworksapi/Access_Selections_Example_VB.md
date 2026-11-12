---
title: "Access Selections Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_Selections_Example_VB.htm"
---

# Access Selections Example (VBA)

## Access Data Example (VBA)

[View Code](Access_Selections_Example_VB_Code.htm)

All features have a feature data object that contains specific information about each instance of the feature. For example, an extrude feature contains an IExtrudeFeatureData2 object that contains the parameters for the extrude's depth. The IExtrudeFeatureData2::AccessSelections method is called to allow a program to modify a feature data object. After making the changes, call IFeature::ModifyDefinition to implement the changes to the feature and release control of the feature data object. A call to IExtrudeFeatureData2::ReleaseSelectionAccess also releases control of the feature data object.

This example shows how to access and modify the data specific to a certain feature in a SOLIDWORKS part or assembly. To use this example, open a part with a base extrusion and select the base extrusion.

1. Attach the program to SOLIDWORKS, get the active model, and access the ISelectionManager.

  ```vb
  Set swApp = CreateObject("sldWorks.application")
  Set Model = swApp.ActiveDoc
  Set SelMgr = Model.SelectionManager
  ```
2. Obtain the selected feature, and extract the feature data Object from the feature.

  ```vb
  Set CurFeature = SelMgr.GetSelectedObject5(1)
  Set FeatData = CurFeature.GetDefinition
  ```
3. Get the permissions to access the parameters of the feature.

  ```vb
  isGood = FeatData.AccessSelections(Model, Component)
  ```
4. Modify the feature data, in this case double the depth of the extrude.

  ```vb
  Depth = FeatData.GetDepth(True)
  FeatData.SetDepth True, Depth * 2
  ```
5. Implement the changes in the model.

  ```vb
  isGood = CurFeature.ModifyDefinition(FeatData, Model, Component)
  ```
6. If the Feature::ModifyDefinition call fails for any reason, release the access permissions for the feature data.

  ```vb
  FeatData.ReleaseSelectionAccess
  ```
