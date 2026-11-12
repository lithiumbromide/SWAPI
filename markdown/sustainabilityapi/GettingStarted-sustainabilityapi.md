---
title: "Getting Started"
project: "SOLIDWORKS Sustainability API Help"
interface: ""
member: ""
kind: "topic"
source: "sustainabilityapi/GettingStarted-sustainabilityapi.html"
---

# Getting Started

Writing a SOLIDWORKS Sustainability API application typically involves:

1. Adding a reference to either the SOLIDWORKS Sustainability API type library or primary interop assembly:

  - VBA: **sustainability** `version` **Type Library** or `install_dir`\**sustainability.tlb**.
  - C# or VB.NET: **SOLIDWORKS.Interop.sustainability** or `install_dir`\**api\redist\SOLIDWORKS.Interop.sustainability.dll**.
    **NOTE**: `install_dir` is typically **C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS**.
2. Opening a part or assembly document in SOLIDWORKS Design.
3. Getting the model document object, [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html).
4. Calling [IModelDocExtension::GetSustainability](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetSustainability.html) to get the entry point to the SOLIDWORKS Sustainability API, [ISustainabilityApp](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityApp.html).
5. Getting and setting environmental impact factors:

  | For SOLIDWORKS Design document type... | To get or set this environmental impact factor... | Call... |
  | --- | --- | --- |
  | Parts | Material | ISustainabilityApp::GetSustainabilityMaterial |
  |  | Manufacture | ISustainabilityApp::GetSustainabilityManufacturing |
  |  | Region of use | ISustainabilityApp::GetSustainabilityPartUse |
  |  | Transportation | ISustainabilityApp::GetSustainabilityTransportation |
  |  | End of Life | ISustainabilityApp::GetSustainabilityEndOfLife |
  |  |  |  |
  | Assemblies | Material of components | ISustainabilityApp::GetSustainabilityMaterial |
  |  | Manufacture of components | ISustainabilityApp::GetSustainabilityManufacturing |
  |  | Assembly | ISustainabilityApp::GetSustainabilityAssemblyProcess |
  |  | Region of use and energy consumption | ISustainabilityApp::GetSustainabilityAssemblyUse |
  |  | Transportation | ISustainabilityApp::GetSustainabilityTransportation |
  |  | End of Life | ISustainabilityApp::GetSustainabilityEndOfLife |
6. Specifying the [amount of product use time](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationOfUse.html) over which to evaluate environmental impact.
7. Specifying the [units](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationType.html) of time over which to evaluate environmental impact.
8. [Updating the environmental impact results](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.html).
9. Obtaining the environmental impact of a part or assembly in terms of [air acidification](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetAirAcidification.html), [carbon footprint](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetCurrentCarbonFootPrint.html), [energy consumption](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetEnergyConsumption.html), and [water eutrophication](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~GetWaterEutrophication.html).

For more information about SOLIDWORKS Sustainability, see the SOLIDWORKS Design Help.
