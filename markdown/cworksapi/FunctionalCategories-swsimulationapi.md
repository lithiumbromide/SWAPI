---
title: "Functional Categories"
project: "SOLIDWORKS Simulation API Help"
interface: ""
member: ""
kind: "topic"
source: "cworksapi/FunctionalCategories-swsimulationapi.html"
---

# Functional Categories

This topic lists the SOLIDWORKS Simulation interfaces categorized by functionality.

- [SOLIDWORKS Simulation Interface](#SOLIDWORKSSimulation)
- [Model Document Interface](#ModelDocument)
- [Studies Interfaces](#Studies)
- [Solids Interfaces](#Solids)
- [Shells Interfaces](#Shells)
- [Contacts Interfaces](#Contacts)
- [Loads and Restraints Interfaces](#LoadsAndRestraints)
- [Mass Properties Interface](#MassProperties)
- [Materials Interface](#Materials)
- [Mesh Interfaces](#Mesh)
- [Beam Interfaces](#Beams)
- [Results Interface](#Results)
- [Topology Interfaces](#Topology)

**NOTE:** Interfaces appear in alphabetical order on the Contents tab in the interop assembly namespace book.

##### SOLIDWORKS Simulation Interface

- [ICosmosWorks](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICosmosWorks.html)

##### Model Document Interface

- [ICWModelDoc](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWModelDoc.html)

##### Studies Interfaces

- [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html)
- [ICWFatigueEvent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueEvent.html)
- [ICWStudy](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy.html)
- [ICWStudyManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyManager.html)
- [ICWTrendTracker](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTrendTracker.html)
- Options
- - [ICWBucklingStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions.html)
  - [ICWDampingOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions.html)
  - [ICWDropTestStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestStudyOptions.html)
  - [ICWDropTestResultOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestResultOptions.html)
  - [ICWDynamicStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions.html)
  - [ICWFatigueStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFatigueStudyOptions.html)
  - [ICWFrequencyStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html)
  - [ICWNonLinearStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html)
  - [ICWRunSpecStudiesRunMeshOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html)
  - [ICWStaticStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html)
  - [ICWStudyResultOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions.html)
  - [ICWThermalStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWThermalStudyOptions.html)

[Back to top](#Top)

##### Solids Interfaces

- [ICWSolidBody](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidBody.html)
- [ICWSolidComponent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidComponent.html)
- [ICWSolidManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidManager.html)

[Back to top](#Top)

##### Shells Interfaces

- [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
- [ICWShell](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShell.html)
- [ICWShellManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWShellManager.html)

[Back to top](#Top)

##### Contacts Interfaces

- [ICWContactComponent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactComponent.html)
- [ICWContactManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager.html)
- [ICWContactSet](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html)
- [ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
- [ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)

[Back to top](#Top)

##### Loads and Restraints Interfaces

- [ICWLoadCaseManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadCaseManager.html)
- [ICWLoadsAndRestraints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraints.html)
- [ICWLoadsAndRestraintsManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
- [ICWRestraint](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRestraint.html)
- [ICWBaseExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBaseExcitation.html)
- [ICWDynamicInitialCondition](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicInitialCondition.html)
- Connectors

  - [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
  - [ICWBoltConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBoltConnector.html)
  - [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
  - [ICWEdgeWeldConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWEdgeWeldConnector.html)
  - [ICWElasticConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWElasticConnector.html)
  - [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
  - [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
  - [ICWLinkConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLinkConnector.html)
  - [ICWPinConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPinConnector.html)
  - [ICWRigidConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRigidConnector.html)
  - [ICWSpotWeldConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpotWeldConnector.html)
  - [ICWSpringConnector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSpringConnector.html)
- Structural Loads

  - [ICWBearingLoad](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBearingLoad.html)
  - [ICWCentriFugalForce](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWCentriFugalForce.html)
  - [ICWDistributedMass](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDistributedMass.html)
  - [ICWForce](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWForce.html)
  - [ICWGravity](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWGravity.html)
  - [ICWPressure](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPressure.html)
  - [ICWRemoteLoad](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRemoteLoad.html)
- Thermal Loads

  - [ICWConvection](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWConvection.html)
  - [ICWHeatFlux](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatFlux.html)
  - [ICWHeatPower](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatPower.html)
  - [ICWRadiation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRadiation.html)
  - [ICWTemperature](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWTemperature.html)

[Back to top](#Top)

##### Topology Interfaces

- [ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
- [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
- [ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html)
- [ICWTopologyFrequencyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html)
- [ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html)
- [ICWTopologyMinimizeMaximumDisplacementGoal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMinimizeMaximumDisplacementGoal.html)
- [ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
- [ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html)
- [ICWTopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html)
- [ICWTopologyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)
- [ICWTopologySymmetryControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologySymmetryControl.html)
- [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)

[Back to top](#Top)

##### Mass Properties Interface

- [ICWMassPropertiesManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMassPropertiesManager.html)

[Back to top](#Top)

##### Materials Interface

- [ICWMaterial](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

[Back to top](#Top)

##### Mesh Interfaces

- [ICWMesh](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMesh.html)
- [ICWMeshControl](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMeshControl.html)

[Back to top](#Top)

##### Beam Interfaces

- [ICWBeamBody](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody.html)
- [ICWBeamManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamManager.html)
- [ICWJoints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints.html)

[Back to top](#Top)

##### Results Interfaces

- [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
- [ICWResults](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults.html)
- [ICWResultsProbeManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html)
- [ICWRunStudiesResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html)

[Back to top](#Top)
