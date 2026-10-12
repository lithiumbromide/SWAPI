---
title: "ICWLoadsAndRestraintsManager Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html"
---

# ICWLoadsAndRestraintsManager Interface Members

The following tables list the members exposed by [ICWLoadsAndRestraintsManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Count | Gets the number of loads and restraints defined in the active study. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddBearingConnector | Adds the specified bearing connector. |
| Method | AddBearingLoad | Adds a bearing load. |
| Method | AddBoltConnector | Adds a bolt connector. |
| Method | AddCable | Adds a cable. |
| Method | AddCentrifugalForce | Creates a centrifugal force. |
| Method | AddConvection | Creates a convection load for thermal studies. |
| Method | AddCyclicSymmetryRestraint | Adds a cyclic symmetry restraint. |
| Method | AddDistributedMass | Creates a distributed mass. |
| Method | AddEdgeWeldConnector | Creates the specified edge weld connector. |
| Method | AddElasticConnector | Adds an elastic support fixture. |
| Method | AddForce | Obsolete. Superseded by ICWLoadsAndRestraintsManager::AddForce2 . |
| Method | AddForce2 | Obsolete. Superseded by ICWloadsAndRestraintsManager::AddForce3 . |
| Method | AddForce3 | Creates a force. |
| Method | AddGeneralSpringConnector | Adds a general spring connector. |
| Method | AddGravity | Adds a gravity load. |
| Method | AddHeatFlux | Creates a heat flux load for thermal studies. |
| Method | AddHeatPower | Creates a heat power load for thermal studies. |
| Method | AddInitialConditionForDynamicStudy | Obsolete. Superseded by ICWLoadsAndRestraintsManager::AddInitialConditionForDynamicStudy2 . |
| Method | AddInitialConditionForDynamicStudy2 | Creates the initial (time = 0) condition for displacements, velocities, or accelerations in modal time history and nonlinear dynamic studies. |
| Method | AddLinkageRod | Adds the specified linkage rod connector. |
| Method | AddLinkConnector | Adds a link connector. |
| Method | AddPinConnector | Adds a pin connector. |
| Method | AddPrescribedDisplacement | Applies the specified prescribed displacement to the specified geometric entities to create a fixture. |
| Method | AddPressure | Creates pressure. |
| Method | AddRadiation | Creates a radiation load for thermal studies. |
| Method | AddRemoteLoad | Creates a remote load of the specified type at the specified location. |
| Method | AddRestraint | Creates a restraint. |
| Method | AddRigidConnector | Adds a rigid connector. |
| Method | AddSelectedBaseExcitation | Obsolete. Superseded by ICWLoadsAndRestraintsManager::AddSelectedBaseExcitation2 . |
| Method | AddSelectedBaseExcitation2 | Applies a base excitation to the specified restraint along the specified directions for dynamic studies. |
| Method | AddSpotWeldConnector | Adds a spot weld connector. |
| Method | AddSpringConnector | Adds a spring connector. |
| Method | AddTemperature | Creates a temperature load for thermal studies. |
| Method | AddUniformBaseExcitation | Obsolete. Superseded by ICWLoadsAndRestraintsManager::AddUniformBaseExcitation2 . |
| Method | AddUniformBaseExcitation2 | Adds a uniform base excitation to all locations restrained in the specified directions for dynamic studies. |
| Method | CopyLoadsAndRestraintsToStudy | Copies the specified loads and restraints to the specified study. |
| Method | DeleteLoadsAndRestraints | Deletes a load or restraint. |
| Method | GetBearingConnector | Gets the specified bearing connector. |
| Method | GetCable | Gets the specified cable. |
| Method | GetEdgeWeldConnector | Gets the edge weld connector at the specified index. |
| Method | GetGeneralSpringConnector | Gets the specified general spring connector. |
| Method | GetLinkageRod | Gets the specified linkage rod connector. |
| Method | GetLoadsAndRestraints | Gets the load or restraint at the specified index. |

[Top](#topBookmark)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWLoadsAndRestraints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html)
