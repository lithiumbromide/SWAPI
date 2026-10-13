---
title: "DeleteDefaultFatigueStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "DeleteDefaultFatigueStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultFatigueStudyPlot.html"
---

# DeleteDefaultFatigueStudyPlot Method (ICWModelDoc)

Deletes the specified default fatigue study plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDefaultFatigueStudyPlot( _
   ByVal NResultType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NResultType As System.Integer
Dim value As System.Integer

value = instance.DeleteDefaultFatigueStudyPlot(NResultType)
```

### C#

```csharp
System.int DeleteDefaultFatigueStudyPlot(
   System.int NResultType
)
```

### C++/CLI

```cpp
System.int DeleteDefaultFatigueStudyPlot(
   System.int NResultType
)
```

### Parameters

- `NResultType`: Type of fatigue study result plot to delete as defined by [swsFatigueStudyResultType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsFatigueStudyResultType_e.html)

### Return Value

Error code as defined in [swsResultPlotDelete_ErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotDelete_ErrorCode_e.html)

## VBA Syntax

See [CWModelDoc::DeleteDefaultFatigueStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~DeleteDefaultFatigueStudyPlot.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::AddDefaultFatigueStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultFatigueStudyPlot.html)
[ICWModelDoc::DeleteAllDefaultFatigueStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultFatigueStudyPlots.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
