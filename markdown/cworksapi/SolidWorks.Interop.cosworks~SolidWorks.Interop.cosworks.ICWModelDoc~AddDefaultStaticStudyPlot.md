---
title: "AddDefaultStaticStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "AddDefaultStaticStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultStaticStudyPlot.html"
---

# AddDefaultStaticStudyPlot Method (ICWModelDoc)

Specifies a default static study result plot for the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDefaultStaticStudyPlot( _
   ByVal NResultType As System.Integer, _
   ByVal NResultComponent As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NResultType As System.Integer
Dim NResultComponent As System.Integer
Dim value As System.Integer

value = instance.AddDefaultStaticStudyPlot(NResultType, NResultComponent)
```

### C#

```csharp
System.int AddDefaultStaticStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### C++/CLI

```cpp
System.int AddDefaultStaticStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### Parameters

- `NResultType`: Type of static study result to plot as defined by [swsDefaultStaticResultTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDefaultStaticResultTypes_e.html)
- `NResultComponent`:

  | If NResultType is swsDefaultStaticResultTypes_e... | Then NResultComponent is... |
  | --- | --- |
  | swsStaticResultDisplacement | Displacement to plot as defined by swsStaticResultDisplacementComponentTypes_e |
  | swsStaticResultElementalStrain | Elemental strain to plot as defined by swsStaticResultElementalStrainComponentTypes_e |
  | swsStaticResultElementalStress | Elemental stress to plot as defined by swsStaticResultElementalStressComponentTypes_e |
  | swsStaticResultNodalStrain | Nodal strain to plot as defined by swsStaticResultNodalStrainComponentTypes_e |
  | swsStaticResultNodalStress | Nodal stress to plot as defined by swsStaticResultNodalStressComponentTypes_e |
  | swsStaticResultBoltPinCheck | Not valid |
  | swsStaticResultFactorOfSafety | Not valid |

### Return Value

Error code as defined by [swsAddDefaultStaticStudyPlotResultError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAddDefaultStaticStudyPlotResultError_e.html)

## VBA Syntax

See [CWModelDoc::AddDefaultStaticStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~AddDefaultStaticStudyPlot.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::DeleteAllDefaultStaticStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultStaticStudyPlots.html)
[ICWModelDoc::DeleteDefaultStaticStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultStaticStudyPlot.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
