---
title: "DeleteDefaultDropTestStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "DeleteDefaultDropTestStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultDropTestStudyPlot.html"
---

# DeleteDefaultDropTestStudyPlot Method (ICWModelDoc)

Deletes the specified default drop test study plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDefaultDropTestStudyPlot( _
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

value = instance.DeleteDefaultDropTestStudyPlot(NResultType, NResultComponent)
```

### C#

```csharp
System.int DeleteDefaultDropTestStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### C++/CLI

```cpp
System.int DeleteDefaultDropTestStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### Parameters

- `NResultType`: Type of drop test study result plot to delete as defined by [swsDropTestStudyResultType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropTestStudyResultType_e.html)
- `NResultComponent`:

  | If NResultType is swsDropTestStudyResultType_e... | Then NResultComponent is... |
  | --- | --- |
  | swsDropTestResultDisplacement | Displacement component to plot as defined by swsDisplacementComponent_e |
  | swsDropTestResultElementalStrain | Strain component to plot as defined by swsStrainComponent_e |
  | swsDropTestResultElementalStress or swsDropTestResultNodalStress | Stress component to plot as defined by swsStressComponent_e |

### Return Value

Error code as defined in [swsResultPlotDelete_ErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotDelete_ErrorCode_e.html)

## VBA Syntax

See [CWModelDoc::DeleteDefaultDropTestStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~DeleteDefaultDropTestStudyPlot.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::AddDefaultDropTestStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultDropTestStudyPlot.html)
[ICWModelDoc::DeleteAllDefaultDropTestStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultDropTestStudyPlots.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
