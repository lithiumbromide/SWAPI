---
title: "CaptureProbedResultPlotAsPNGImage Method (ICWResultsProbeManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResultsProbeManager"
member: "CaptureProbedResultPlotAsPNGImage"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager~CaptureProbedResultPlotAsPNGImage.html"
---

# CaptureProbedResultPlotAsPNGImage Method (ICWResultsProbeManager)

Saves the probed results plot as a PNG image in the specified file and folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function CaptureProbedResultPlotAsPNGImage( _
   ByVal SImageFolder As System.String, _
   ByVal SImageName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResultsProbeManager
Dim SImageFolder As System.String
Dim SImageName As System.String
Dim value As System.Integer

value = instance.CaptureProbedResultPlotAsPNGImage(SImageFolder, SImageName)
```

### C#

```csharp
System.int CaptureProbedResultPlotAsPNGImage(
   System.string SImageFolder,
   System.string SImageName
)
```

### C++/CLI

```cpp
System.int CaptureProbedResultPlotAsPNGImage(
   System.String^ SImageFolder,
   System.String^ SImageName
)
```

### Parameters

- `SImageFolder`: Name of folder to which to save the image
- `SImageName`: Name of file to which to save the image

### Return Value

Error code as defined in [swsProbePostResultErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultErrorCode_e.html)

## VBA Syntax

See [CWResultsProbeManager::CaptureProbedResultPlotAsPNGImage](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResultsProbeManager~CaptureProbedResultPlotAsPNGImage.html).

## Examples

See the [ICWResultsProbeManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html) examples.

## See Also

[ICWResultsProbeManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html)
[ICWResultsProbeManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
