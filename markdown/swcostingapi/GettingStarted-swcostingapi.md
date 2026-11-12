---
title: "Getting Started"
project: "SOLIDWORKS Costing API Help"
interface: ""
member: ""
kind: "topic"
source: "swcostingapi/GettingStarted-swcostingapi.html"
---

# Getting Started

Writing a SOLIDWORKS Costing API application typically involves:

1. Adding a reference to either the SOLIDWORKS Costing API type library or primary interop assembly:

  - VBA: **SldCostingAPI** `version` **Type Library** or `install_dir`\**sldcostingapi.tlb**.
  - C# or VB.NET: **SolidWorks.Interop.sldcostingapi** or `install_dir`\**api\redist\SolidWorks.Interop.sldcostingapi.dll**.

    **NOTE**: `install_dir` is usually **C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS**.
2. Opening the part for the Costing analysis.
3. Getting or setting the Costing template folders and Costing Report template folders using ISldWorks::GetUserPreferenceStringValue or ISldWorks::SetUserPreferenceStringValue (see **Templates**).
4. Getting the model document, [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object.
5. Getting the CostingManager, [ICostManager](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostManager.html) object, and getting the Costing templates.
6. Getting the Costing model, [ICostPart](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart.html) object.
7. Getting the Costing bodies, [ICostBody](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostBody.html) objects.
8. Creating or getting the common Costing analysis, [ICostAnalysis](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis.html) object, and getting and setting its analysis data.
9. Creating or getting each Costing body's specific Costing analysis.
10. Getting each Costing feature or subfeature, [ICostFeature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature.html) object, and getting or setting its analysis data.

### Templates

The SOLIDWORKS Costing tool provides templates that associate manufacturing features with their costs. The templates include information about material, machining, and labor costs. After the manufacturing features are recognized, Costing categorizes each manufacturing feature and applies the correct information from the template to cost out the specific manufacturing features. A total cost for all of the features is tabulated and a final unit cost is returned. You can also create reports of Costing results using the SOLIDWORKS Costing tool. The detailed line items in the report help you determine the impact of design decisions on cost.

To get or set the file locations for Costing templates and Costing report templates, you can use the SOLIDWORKS API and call [ISldWorks::GetUserPreferenceStringValue](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html) or [ISldWorks::SetUserPreferenceStringValue](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.html) with:

- [swUserPreferenceStringValue_e.swFileLocationsCostingTemplates](ms-its:swconst.chm::/SO_FileLocations.htm#Costing) for Costing templates.
- [swUserPreferenceStringValue_e.swFileLocationsCostingReportTemplateFolder](ms-its:swconst.chm::/SO_FileLocations.htm#CostingReport) for Costing report templates.

For more information about SOLIDWORKS Costing and its templates, see the SOLIDWORKS Design Help.
