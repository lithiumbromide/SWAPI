---
title: "ShowAnnotationsOnNodesOrElems Method (ICWResultsProbeManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResultsProbeManager"
member: "ShowAnnotationsOnNodesOrElems"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager~ShowAnnotationsOnNodesOrElems.html"
---

# ShowAnnotationsOnNodesOrElems Method (ICWResultsProbeManager)

Shows results probe annotations for the specified nodes or elements.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowAnnotationsOnNodesOrElems( _
   ByVal SSelectedNodesOrElems As System.String, _
   ByRef ArrayAnnotationWarnings As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResultsProbeManager
Dim SSelectedNodesOrElems As System.String
Dim ArrayAnnotationWarnings As System.Object
Dim value As System.Integer

value = instance.ShowAnnotationsOnNodesOrElems(SSelectedNodesOrElems, ArrayAnnotationWarnings)
```

### C#

```csharp
System.int ShowAnnotationsOnNodesOrElems(
   System.string SSelectedNodesOrElems,
   out System.object ArrayAnnotationWarnings
)
```

### C++/CLI

```cpp
System.int ShowAnnotationsOnNodesOrElems(
   System.String^ SSelectedNodesOrElems,
   [Out] System.Object^ ArrayAnnotationWarnings
)
```

### Parameters

- `SSelectedNodesOrElems`: Comma-delimited string of nodes or elements, e.g., "1,25,30-35"
- `ArrayAnnotationWarnings`: Array of warnings for specified nodes or elements as defined in [swsProbePostResultNodeElementSelectionWarning_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultNodeElementSelectionWarning_e.html)

### Return Value

0 if successful; otherwise error code as defined in [swsProbePostResultErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultErrorCode_e.html)

## VBA Syntax

See [CWResultsProbeManager::ShowAnnotationsOnNodesOrElems](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResultsProbeManager~ShowAnnotationsOnNodesOrElems.html).

## See Also

[ICWResultsProbeManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html)
[ICWResultsProbeManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP3
