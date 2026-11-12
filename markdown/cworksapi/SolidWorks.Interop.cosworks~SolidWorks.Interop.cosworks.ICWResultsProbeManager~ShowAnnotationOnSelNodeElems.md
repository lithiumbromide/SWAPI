---
title: "ShowAnnotationOnSelNodeElems Method (ICWResultsProbeManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResultsProbeManager"
member: "ShowAnnotationOnSelNodeElems"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager~ShowAnnotationOnSelNodeElems.html"
---

# ShowAnnotationOnSelNodeElems Method (ICWResultsProbeManager)

Obsoleted. Superseded by [ICWResultsProbeManager::ShowAnnotationsOnNodesOrElems](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager~ShowAnnotationsOnNodesOrElems.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowAnnotationOnSelNodeElems( _
   ByVal ArraySelectedNodeElems As System.Object, _
   ByRef ArrayAnnotationWarnings As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResultsProbeManager
Dim ArraySelectedNodeElems As System.Object
Dim ArrayAnnotationWarnings As System.Object
Dim value As System.Integer

value = instance.ShowAnnotationOnSelNodeElems(ArraySelectedNodeElems, ArrayAnnotationWarnings)
```

### C#

```csharp
System.int ShowAnnotationOnSelNodeElems(
   System.object ArraySelectedNodeElems,
   out System.object ArrayAnnotationWarnings
)
```

### C++/CLI

```cpp
System.int ShowAnnotationOnSelNodeElems(
   System.Object^ ArraySelectedNodeElems,
   [Out] System.Object^ ArrayAnnotationWarnings
)
```

### Parameters

- `ArraySelectedNodeElems`: Array of nodes or elements
- `ArrayAnnotationWarnings`: Array of warnings for specified nodes or elements as defined in [swsProbePostResultNodeElementSelectionWarning_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultNodeElementSelectionWarning_e.html)

### Return Value

Error code as defined in [swsProbePostResultErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultErrorCode_e.html)

## VBA Syntax

See [CWResultsProbeManager::ShowAnnotationOnSelNodeElems](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResultsProbeManager~ShowAnnotationOnSelNodeElems.html).

## Examples

See the [ICWResultsProbeManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html) examples.

## See Also

[ICWResultsProbeManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html)
[ICWResultsProbeManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
