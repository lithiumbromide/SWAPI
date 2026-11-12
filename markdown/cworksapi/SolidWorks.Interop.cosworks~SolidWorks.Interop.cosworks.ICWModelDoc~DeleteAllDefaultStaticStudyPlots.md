---
title: "DeleteAllDefaultStaticStudyPlots Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "DeleteAllDefaultStaticStudyPlots"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultStaticStudyPlots.html"
---

# DeleteAllDefaultStaticStudyPlots Method (ICWModelDoc)

Deletes all default static study plots from this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteAllDefaultStaticStudyPlots() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim value As System.Integer

value = instance.DeleteAllDefaultStaticStudyPlots()
```

### C#

```csharp
System.int DeleteAllDefaultStaticStudyPlots()
```

### C++/CLI

```cpp
System.int DeleteAllDefaultStaticStudyPlots();
```

### Return Value

Error code as defined in [swsResultPlotDelete_ErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotDelete_ErrorCode_e.html)

## VBA Syntax

See [CWModelDoc::DeleteAllDefaultStaticStudyPlots](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~DeleteAllDefaultStaticStudyPlots.html).

## Examples

[Create Plots for a Static Study (VBA)](Create_Plots_for_Static_Study_Example_VB.htm)
[Create Plots for a Static Study (VB.NET)](Create_Plots_for_Static_Study_Example_VBNET.htm)
[Create Plots for a Static Study (C#)](Create_Plots_for_Static_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::AddDefaultStaticStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultStaticStudyPlot.html)
[ICWModelDoc::DeleteDefaultStaticStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultStaticStudyPlot.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
