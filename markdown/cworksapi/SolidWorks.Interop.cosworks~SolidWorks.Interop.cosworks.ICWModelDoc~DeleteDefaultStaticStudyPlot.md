---
title: "DeleteDefaultStaticStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "DeleteDefaultStaticStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultStaticStudyPlot.html"
---

# DeleteDefaultStaticStudyPlot Method (ICWModelDoc)

Deletes the specified default static study plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDefaultStaticStudyPlot( _
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

value = instance.DeleteDefaultStaticStudyPlot(NResultType, NResultComponent)
```

### C#

```csharp
System.int DeleteDefaultStaticStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### C++/CLI

```cpp
System.int DeleteDefaultStaticStudyPlot(
   System.int NResultType,
   System.int NResultComponent
)
```

### Parameters

- `NResultType`: Type of static study result plot to delete as defined by [swsDefaultStaticResultTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDefaultStaticResultTypes_e.html)
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

Error code as defined in [swsResultPlotDelete_ErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotDelete_ErrorCode_e.html)

## VBA Syntax

See [CWModelDoc::DeleteDefaultStaticStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~DeleteDefaultStaticStudyPlot.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::AddDefaultStaticStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultStaticStudyPlot.html)
[ICWModelDoc::DeleteAllDefaultStaticStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultStaticStudyPlots.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
