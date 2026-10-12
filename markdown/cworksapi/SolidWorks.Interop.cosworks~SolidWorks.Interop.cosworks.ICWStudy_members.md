---
title: "ICWStudy Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html"
---

# ICWStudy Interface Members

The following tables list the members exposed by [ICWStudy](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AnalysisType | Gets the type of the analysis of the active study. |
| Property | BeamManager | Gets the beam manager. |
| Property | BucklingStudyOptions | Gets the options for this buckling study. |
| Property | ConfigurationName | Gets the name of the study's configuration. |
| Property | ContactManager | Gets the contact manager. |
| Property | DampingOptions | Gets the damping options for this study. |
| Property | DropTestResultOptions | Gets the result options for this drop test study. |
| Property | DropTestSetup | Gets the setup for this drop test study. |
| Property | DropTestStudyOptions | Gets the options for this drop test study. |
| Property | DynamicAnalysisSubType | Gets the type of this linear dynamic analysis. |
| Property | DynamicStudyOptions | Gets the options for this dynamic study. |
| Property | FatigueStudyOptions | Gets the options for this fatigue study. |
| Property | FrequencyStudyOptions | Gets the options for this frequency study. |
| Property | IsSimulationDistributable | Gets whether this study supports network simulation. |
| Property | LoadCaseManager | Gets the Load Case Manager for this static study. |
| Property | LoadsAndRestraintsManager | Gets the loads and restraints manager. |
| Property | Mesh | Gets the mesh of this study. |
| Property | MeshType | Gets the mesh type of this study. |
| Property | MultipleComponentContactsEditManager | Gets the Multiple Component Contacts Edit Manager which provides the simultaneous editing of multiple component contacts. |
| Property | MultipleContactSetsEditManager | Gets the Multiple Contact Sets Edit Manager which provides the simultaneous editing of multiple contact sets. |
| Property | Name | Gets the name of this study. |
| Property | NonlinearAnalysisSubType | Gets the subtype of this nonlinear study. |
| Property | NonLinearStudyOptions | Gets the options for this nonlinear study. |
| Property | OffLoad | Gets or sets whether to offload the coordinating computer's simulation processing to other computers on the network. |
| Property | Results | Gets the results of this study. |
| Property | ShellManager | Gets the shell manager. |
| Property | ShowOrHideFixtures | Shows or hides fixture symbols in the graphics area. |
| Property | ShowOrHideForce | Shows or hides the force symbols in the graphics area. |
| Property | SolidManager | Gets the solid manager. |
| Property | StaticStudyOptions | Gets the options for this static study. |
| Property | StudyResultOptions | Gets the result options for this study. |
| Property | SwxDRDOneClickWorkflowInfo | *Internal use only* |
| Property | ThermalStudyOptions | Gets the options for this thermal study. |
| Property | TopologyStudyManager | Gets the manager of this topology study's goals, constraints, and manufacturing controls. |
| Property | TopologyStudyOptions | Gets this topology study's options. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivateConfiguration | Activates the configuration of this study. |
| Method | AddDropTestSetup | Adds a setup to this drop test study. |
| Method | CopyMeshFromStudy | Copies the mesh from the specified study to this study. |
| Method | CreateImportedResultsPlot | Creates a plot for this study using the specified external results file. |
| Method | CreateMesh | Creates the mesh. |
| Method | CreateMeshForMeshControl | Creates a mesh for the specified mesh control. |
| Method | CreateTrendTracker | Creates a Trend Tracker for this study. |
| Method | DeleteTrendTracker | Deletes the Trend Tracker from this study. |
| Method | ExportSimulationStudy | Exports this study to the specified finite-element analysis program. |
| Method | GenerateReport | Creates a report about all aspects of this study. |
| Method | GetClusterComputers | Gets the list of names of the computers participating in this study's distributed simulation. |
| Method | GetMassPropertiesManager | Gets the mass properties manager. |
| Method | GetTimeTakenForGapIterationsAndContactOperations | Gets the time taken for gap iterations and contact operations in this nonlinear study. |
| Method | GetTimeTakenForInputDataTransferFromDatabase | Gets the time taken for input data transfer from the database in this nonlinear study. |
| Method | GetTimeTakenForInputPhase | Gets the time taken for the input phase of this static study. |
| Method | GetTotalSolutionTime | Gets the total solver time for this study. |
| Method | ImportStudyFeatures | Imports the study features of the specified component's study into this study. |
| Method | MeshAndRun | Meshes the model and analyzes the study. |
| Method | RunAnalysis | Runs this study. |
| Method | SetClusterComputers | Sets the list of names of the computers participating in this study's distributed simulation. |
| Method | SetFatigueResultOptions | Sets the result options for this fatigue study. |
| Method | SetNonLinearStudyOptions | Sets the nonlinear study options. |
| Method | SetResultCombinationSetup | Sets the result combination setup for this Pressure Vessel Design study. |
| Method | UpdateAllComponents | Updates all components in the active study |

[Top](#topBookmark)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
