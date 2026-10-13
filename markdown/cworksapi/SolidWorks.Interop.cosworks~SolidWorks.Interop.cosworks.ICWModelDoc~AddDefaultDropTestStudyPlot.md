---
title: "AddDefaultDropTestStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "AddDefaultDropTestStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultDropTestStudyPlot.html"
---

# AddDefaultDropTestStudyPlot Method (ICWModelDoc)

Specifies a default drop test study result plot for the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDefaultDropTestStudyPlot( _
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

value = instance.AddDefaultDropTestStudyPlot(NResultType, NResultComponent)
```

### C#

```csharp
System.int AddDefaultDropTestStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### C++/CLI

```cpp
System.int AddDefaultDropTestStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### Parameters

- `NResultType`: Type of drop test study result to plot as defined by [swsDropTestStudyResultType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropTestStudyResultType_e.html)
- `NResultComponent`:

  | If NResultType is swsDropTestStudyResultType_e... | Then NResultComponent is... |
  | --- | --- |
  | swsDropTestResultDisplacement | Displacement component to plot as defined by swsDisplacementComponent_e |
  | swsDropTestResultElementalStrain | Strain component to plot as defined by swsStrainComponent_e |
  | swsDropTestResultElementalStress or swsDropTestResultNodalStress | Stress component to plot as defined by swsStressComponent_e |

### Return Value

Error code as defined by [swsAddDefaultDropTestStudyPlotResultError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAddDefaultDropTestStudyPlotResultError_e.html)

## VBA Syntax

See [CWModelDoc::AddDefaultDropTestStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~AddDefaultDropTestStudyPlot.html).

## Examples

[Create Drop Test Study (VBA)](Create_Drop_Test_Study_Example_VB.htm)
[Create Drop Test Study (VB.NET)](Create_Drop_Test_Study_Example_VBNET.htm)
[Create Drop Test Study (C#)](Create_Drop_Test_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::DeleteAllDefaultDropTestStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultDropTestStudyPlots.html)
[ICWModelDoc::DeleteDefaultDropTestStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultDropTestStudyPlot.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
