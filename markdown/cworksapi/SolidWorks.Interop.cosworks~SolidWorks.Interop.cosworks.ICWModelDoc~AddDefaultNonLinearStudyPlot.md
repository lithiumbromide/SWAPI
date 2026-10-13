---
title: "AddDefaultNonLinearStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "AddDefaultNonLinearStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultNonLinearStudyPlot.html"
---

# AddDefaultNonLinearStudyPlot Method (ICWModelDoc)

Specifies a default nonlinear study result plot for the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDefaultNonLinearStudyPlot( _
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

value = instance.AddDefaultNonLinearStudyPlot(NResultType, NResultComponent)
```

### C#

```csharp
System.int AddDefaultNonLinearStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### C++/CLI

```cpp
System.int AddDefaultNonLinearStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### Parameters

- `NResultType`: Default nonlinear study result plot types as defined in [swsNonlinearStudyResultTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonlinearStudyResultTypes_e.html)
- `NResultComponent`:

  | If NResultType is ... | Then NResultComponent is... |
  | --- | --- |
  | 0 = Nodal stress or 1 = Elemental stress | Stress component to plot as defined by swsStressComponent_e |
  | 2 = Displacement | Displacement component to plot as defined by swsDisplacementComponent_e |
  | 3 = Nodal strain or 4 = Elemental strain | Strain component to plot as defined by swsStrainComponent_e |

### Return Value

Error code as defined by [swsAddDefaultNonLinearStudyPlotResultError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAddDefaultNonLinearStudyPlotResultError_e.html)

## VBA Syntax

See [CWModelDoc::AddDefaultNonLinearStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~AddDefaultNonLinearStudyPlot.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::DeleteAllDefaultNonLinearStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultNonLinearStudyPlots.html)
[ICWModelDoc::DeleteDefaultNonLinearStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultNonLinearStudyPlot.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
