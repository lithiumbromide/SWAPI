---
title: "DeleteDefaultThermalStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "DeleteDefaultThermalStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultThermalStudyPlot.html"
---

# DeleteDefaultThermalStudyPlot Method (ICWModelDoc)

Deletes the specified default thermal study plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDefaultThermalStudyPlot( _
   ByVal NResultComponent As System.Integer, _
   ByVal BTransient As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NResultComponent As System.Integer
Dim BTransient As System.Boolean
Dim value As System.Integer

value = instance.DeleteDefaultThermalStudyPlot(NResultComponent, BTransient)
```

### C#

```csharp
System.int DeleteDefaultThermalStudyPlot(
   System.int NResultComponent,
   System.bool BTransient
)
```

### C++/CLI

```cpp
System.int DeleteDefaultThermalStudyPlot(
   System.int NResultComponent,
   System.bool BTransient
)
```

### Parameters

- `NResultComponent`: Type of thermal study result plot to delete as defined by [swsThermalResultComponentTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsThermalResultComponentTypes_e.html)
- `BTransient`: True if transient, false if steady state (see **Remarks**)

### Return Value

Error code as defined in [swsResultPlotDelete_ErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotDelete_ErrorCode_e.html)

## VBA Syntax

See [CWModelDoc::DeleteDefaultThermalStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~DeleteDefaultThermalStudyPlot.html).

## Remarks

If BTransient is true, this plot is for a transient thermal study in which an initial temperature profile is defined for the thermal load.

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::AddDefaultThermalStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultThermalStudyPlot.html)
[ICWModelDoc::DeleteAllDefaultThermalStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultThermalStudyPlots.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
