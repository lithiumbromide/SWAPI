---
title: "ICWResults Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html"
---

# ICWResults Interface Members

The following tables list the members exposed by [ICWResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivatePlot | Activates the specified plot. |
| Method | AddIsoClippingToPlot | Adds iso clipping to the specified result plot. |
| Method | CreateAngularRotationPlot | Creates an angular rotation plot for the specified reference axis. |
| Method | CreateDeformedBody | Obsolete. Superseded by ICWResults::CreateDeformedBody2 . |
| Method | CreateDeformedBody2 | Saves the deformed shape that results from running a static or nonlinear study. |
| Method | CreatePlot | Creates the specified plot. |
| Method | CreateResultsEquationPlot | Creates a plot of the specified results equation. |
| Method | CreateStressHotSpotPlot | Creates a stress hot spot plot. |
| Method | DeletePlot | Deletes the specified plot. |
| Method | GetAccelerationComponentForAllStepsAtNode | Gets the acceleration for all solution steps at the specified node for the specified acceleration component. |
| Method | GetAccelerationForEntities | Gets the acceleration for the specified entities, solution step, and acceleration component. |
| Method | GetAverageStressesAtMidnodes | Gets whether to average stress at mid-nodes in this study. |
| Method | GetBeamForcesForEntities | Gets the force values for the specified force for the selected beams. |
| Method | GetBeamMinMaxStress | Gets the minimum and maximum elemental stresses for beams at the specified solution step. |
| Method | GetBeamRadius | Gets the radii of beams used to render the specified plot. |
| Method | GetBeamStressForEntities | Gets the stress values for the specified type of stress for the selected beams. |
| Method | GetBucklingLoadFactors | Gets the buckling load factors. |
| Method | GetConnectorForces | Obsolete. Superseded by ICWResults::GetConnectorForces2 . |
| Method | GetConnectorForces2 | Gets the x-, y-, and z-component and resultant forces, bending moments, and torques for the specified connector and step. |
| Method | GetConnectorForcesWithTimeValue | Gets the component and resultant forces, bending moments, and torques for the specified connector at the specified time. |
| Method | GetContactForcesAndFriction | Gets the specified contact or friction forces for the specified entities. |
| Method | GetDeformedBodyFailedSewOption | Gets the option to use when a deformed body fails to sew into a solid object. |
| Method | GetDeformedCoord | Gets nodal deform coordinates for the specified plot. |
| Method | GetDetectedHotSpotElements | Gets the stress hot spot elements. |
| Method | GetDetectedHotSpotNodes | Gets the stress hot spot nodes. |
| Method | GetDisplacementAtPoints | Gets the specified displacement component at the specified points for the specified solution step. |
| Method | GetDisplacementComponentForAllStepsAtNode | Gets the specified displacement component at the specified node for all solutions steps. |
| Method | GetDisplacementForEntities | Gets the specified displacement component for the specified entities at the specified solution step. |
| Method | GetEdgeWeldResults | Gets the edge weld results for the specified edge weld connector. |
| Method | GetEnvelopeAccelerationForEntities | Gets the specified envelope acceleration for the specified entities across all solution steps. |
| Method | GetEnvelopeDisplacementForEntities | Gets the specified envelope displacement for the specified entities across all solution steps. |
| Method | GetEnvelopeStrainForEntities | Gets the specified envelope strain for the specified entities across all solution steps. |
| Method | GetEnvelopeStressForEntities | Gets the specified envelope stress for the specified entities across all solution steps. |
| Method | GetEnvelopeVelocityForEntities | Gets the specified envelope velocity for the specified entities across all solution steps. |
| Method | GetFactorOfSafetyForComposites | Gets the range of stress or buckling factors of safety for the specified shell type, surface bodies, failure criteria, and other options. |
| Method | GetFatigueForEntities | Gets the specified fatigue component for the specified entities. |
| Method | GetFreeBodyForcesAndMoments | Gets the x-, y-, and z-component and resultant free body forces and moments for the specified entities and the entire model. |
| Method | GetFreeBodyForcesAndMomentsForAStep | Gets the x-, y-, and z-component and resultant free body forces and moments for the specified entities for the specified step. |
| Method | GetHeatPowerOrEnergy | Obsolete. Superseded by ICWResults::GetHeatPowerOrEnergy2 . |
| Method | GetHeatPowerOrEnergy2 | Gets the heat power or heat energy for the specified entities. |
| Method | GetLegendContourColors | Gets the contour colors based on user-input colors. |
| Method | GetLinearizedStressValues | Obsolete. Superseded by ICWPlot::GetLinearizedStressValuesAlongSCL . |
| Method | GetMassParticipation | Gets the mass participation factors in the X, Y, and Z directions for all modes. |
| Method | GetMaximumAvailableSteps | Gets the maximum solution step number for which results exist. |
| Method | GetMinMaxAcceleration | Gets the algebraic minimum and maximum for the specified acceleration component and solution step. |
| Method | GetMinMaxDisplacement | Gets the algebraic minimum and maximum displacement for the specified component and solution step. |
| Method | GetMinMaxDisplacementForHarmonic | Gets the algebraic minimum and maximum displacement for the specified component and solution step of this harmonic study. |
| Method | GetMinMaxDisplacementRMS | Gets the algebraic minimum and maximum displacement RMS values for the specified component of this random vibration study. |
| Method | GetMinMaxFactorOfSafety | Obsolete. Superseded by ICWResults::GetMinMaxFactorOfSafety2 . |
| Method | GetMinMaxFactorOfSafety2 | Gets the algebraic minimum and maximum factors of safety (FOS) for non-composite shells. |
| Method | GetMinMaxFactorOfSafetyWithDetailSettings | Obsolete. Superseded by ICWResults::GetMinMaxFactorOfSafetyWithDetailSettings2 . |
| Method | GetMinMaxFactorOfSafetyWithDetailSettings2 | Gets the algebraic minimum and maximum factors of safety (FOS) for non-composite shells and the specified detail settings. |
| Method | GetMinMaxFatigue | Gets the algebraic minimum and maximum for the specified fatigue component. |
| Method | GetMinMaxResultsEquationValues | Gets the algebraic minimum and maximum from the plot of the specified results equation. |
| Method | GetMinMaxStrain | Gets the algebraic minimum and maximum for the specified strain component, element, and solution step. |
| Method | GetMinMaxStress | Gets the algebraic minimum and maximum for the specified stress component, element, and solution step. |
| Method | GetMinMaxStressForHarmonic | Obsolete. Superseded by ICWResults::GetMinMaxStressForHarmonic2 . |
| Method | GetMinMaxStressForHarmonic2 | Gets the algebraic minimum and maximum for the specified stress component and solution step of this harmonic study. |
| Method | GetMinMaxStressRMS | Gets the algebraic minimum and maximum RMS values for the specified stress component and element of this random vibration study. |
| Method | GetMinMaxThermal | Gets the algebraic minimum and maximum for the specified thermal component and solution step. |
| Method | GetMinMaxVelocity | Gets the algebraic minimum and maximum for the specified velocity component and solution step. |
| Method | GetPlot | Gets the specified results plot. |
| Method | GetPlotColorOptions | Gets the color options for the specified plot. |
| Method | GetPlotCount | Gets the number of plots in this study. |
| Method | GetPlotDefinition | Gets the definition of the specified plot. |
| Method | GetPlotDisplayOptions | Gets the display options for the specified plot. |
| Method | GetPlotNames | Gets the names of the plots for these results. |
| Method | GetPlotPositionFormatOptions | Gets the position format options for the specified plot. |
| Method | GetPlotSettings | Gets the settings for the specified plot. |
| Method | GetPlotSettingsOptionForHiddenAndExcludedBody | Gets hidden and excluded body options for the specified plot. |
| Method | GetReactionForcesAndMoments | Obsolete. Superseded by ICWResults::GetReactionForcesAndMomentsWithSelections . |
| Method | GetReactionForcesAndMomentsWithSelections | Gets the reaction forces and moments for selections and the entire model at the specified solution step. |
| Method | GetRemoteForces | Gets the x-, y-, and z-component and resultant forces applied to selected entities as a result of transferring a remote load in static studies. |
| Method | GetResonantFrequencies | Gets the resonant frequency values. |
| Method | GetResultsEquationValuesForEntities | Gets the result values for the specified equation and selected entities. |
| Method | GetRotationalDisplacement | Gets the rotational displacements at the specified solution step. |
| Method | GetStrain | Gets the strain results for all nodes or elements at the specified solution step. |
| Method | GetStrainComponentForAllStepsAtNode | Gets the specified strain component at the specified node for all solution steps. |
| Method | GetStrainForEntities | Obsolete. Superseded by ICWResults::GetStrainForEntities2 . |
| Method | GetStrainForEntities2 | Obsolete. Superseded by ICWResults::GetStrainForEntities3 . |
| Method | GetStrainForEntities3 | Gets the specified strain component for the specified entities at the specified solution step. |
| Method | GetStress | Gets the stress results for all nodes or elements at the specified solution step. |
| Method | GetStressComponentForAllStepsAtNode | Gets the specified stress component at the specified node for all solution steps. |
| Method | GetStressForEntities | Obsolete. Superseded by ICWResults::GetStressForEntities2 . |
| Method | GetStressForEntities2 | Obsolete. Superseded by ICWResults::GetStressForEntities3 . |
| Method | GetStressForEntities3 | Gets the specified stress component for the specified entities at the specified solution step. |
| Method | GetStressTensorValuesForAllNodesOfElement | Gets the stress tensor values for all nodes of the specified mesh elements at the specified solution step. |
| Method | GetThermalComponentForAllStepsAtNode | Gets thermal values at the specified node for all solutions steps. |
| Method | GetThermalForEntities | Gets thermal values at the specified geometric entities. |
| Method | GetThermalValues | Gets thermal values for all nodes at the specified solution step. |
| Method | GetThermalValuesAtPoints | Gets thermal values at the specified solution step and the specified points. |
| Method | GetTimeOrFrequencyAtEachStep | Obsolete. Superseded by ICWResults::GetTimeOrFrequencyAtEachStep2 . |
| Method | GetTimeOrFrequencyAtEachStep2 | Gets the times or frequencies for all solution steps or mode shapes in these results. |
| Method | GetTranslationalDisplacement | Gets the translational displacements at the specified solution step. |
| Method | GetVelocityComponentForAllStepsAtNode | Gets the specified velocity component for all solution steps at the specified node. |
| Method | GetVelocityForEntities | Gets the specified velocity component for the specified entities and at the specified solution step. |
| Method | IGetPlotNames | Gets the names of the plots in this study. |
| Method | RunStressHotSpotDiagnostics | Obsolete. Superseded by ICWResults::RunStressHotSpotDiagnosticsAndDetectSingularities . |
| Method | RunStressHotSpotDiagnosticsAndDetectSingularities | Detects stress hot spots and singularities. |
| Method | SavePlotsAseDrawings | Saves the specified results plot as an eDrawings file with the specified name in the specified location. |
| Method | SetAverageStressesAtMidnodes | Sets whether to average stresses at mid-nodes for this study. |
| Method | SetDeformedBodyFailedSewOption | Sets the option to use when a deformed body fails to sew into a solid object. |
| Method | SetPlotColorOptions | Sets the color options for the specified plot. |
| Method | SetPlotDisplayOptions | Sets the display options for the specified plot. |
| Method | SetPlotPositionFormatOptions | Sets the position/format options for the specified plot. |
| Method | SetPlotSettings | Sets various settings for the specified plot. |
| Method | SetPlotSettingsOptionForHiddenAndExcludedBody | Sets hidden and excluded body options for the specified plot. |

[Top](#topBookmark)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWResultsProbeManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html)
[ICWRunStudiesResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html)
