---
title: "ExportCSVFile Method (ICosmosMotionStudyResults)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyResults"
member: "ExportCSVFile"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults~ExportCSVFile.html"
---

# ExportCSVFile Method (ICosmosMotionStudyResults)

Exports a plot to a comma-separated value (.csv) formatted file.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportCSVFile( _
   ByVal PlotFeature As System.Object, _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyResults
Dim PlotFeature As System.Object
Dim FileName As System.String
Dim value As System.Boolean

value = instance.ExportCSVFile(PlotFeature, FileName)
```

### C#

```csharp
System.bool ExportCSVFile(
   System.object PlotFeature,
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool ExportCSVFile(
   System.Object^ PlotFeature,
   System.String^ FileName
)
```

### Parameters

- `PlotFeature`: Plot
- `FileName`: Fully qualified path for the the .csv file

### Return Value

True if the plot is exported to a .csv file, false if not

## VBA Syntax

See [CosmosMotionStudyResults::ExportCSVFile](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyResults~ExportCSVFile.html).

## See Also

[ICosmosMotionStudyResults Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults.html)
[ICosmosMotionStudyResults Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyResults_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
