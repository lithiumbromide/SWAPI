---
title: "DeleteDefaultNonLinearStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "DeleteDefaultNonLinearStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultNonLinearStudyPlot.html"
---

# DeleteDefaultNonLinearStudyPlot Method (ICWModelDoc)

Deletes the specified default nonlinear study plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDefaultNonLinearStudyPlot( _
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

value = instance.DeleteDefaultNonLinearStudyPlot(NResultType, NResultComponent)
```

### C#

```csharp
System.int DeleteDefaultNonLinearStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### C++/CLI

```cpp
System.int DeleteDefaultNonLinearStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### Parameters

- `NResultType`: Type of nonlinear study result plot to delete as defined in [swsNonlinearStudyResultTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNonlinearStudyResultTypes_e.html)
- `NResultComponent`:

  | If NResultType is ... | Then NResultComponent is... |
  | --- | --- |
  | 0 = Nodal stress or 1 = Elemental stress | Stress component to plot as defined by swsStressComponent_e |
  | 2 = Displacement | Displacement component to plot as defined by swsDisplacementComponent_e |
  | 3 = Nodal strain or 4 = Elemental strain | Strain component to plot as defined by swsStrainComponent_e |

### Return Value

Error code as defined in [swsResultPlotDelete_ErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotDelete_ErrorCode_e.html)

## VBA Syntax

See [CWModelDoc::DeleteDefaultNonLinearStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~DeleteDefaultNonLinearStudyPlot.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::AddDefaultNonLinearStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultNonLinearStudyPlot.html)
[ICWModelDoc::DeleteAllDefaultNonLinearStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultNonLinearStudyPlots.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
