---
title: "GetDetectedHotSpotNodes Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetDetectedHotSpotNodes"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotNodes.html"
---

# GetDetectedHotSpotNodes Method (ICWResults)

Gets the stress hot spot nodes.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetectedHotSpotNodes( _
   ByRef RetVal As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim RetVal As System.Object
Dim value As System.Integer

value = instance.GetDetectedHotSpotNodes(RetVal)
```

### C#

```csharp
System.int GetDetectedHotSpotNodes(
   out System.object RetVal
)
```

### C++/CLI

```cpp
System.int GetDetectedHotSpotNodes(
   [Out] System.Object^ RetVal
)
```

### Parameters

- `RetVal`: Array of stress hot spot nodes

### Return Value

1 if successful, 0 if not

## VBA Syntax

See [CWResults::GetDetectedHotSpotNodes](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetDetectedHotSpotNodes.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

Before calling this method, you must call [ICWResults::RunStressHotSpotDiagnostics](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~RunStressHotSpotDiagnostics.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDetectedHotSpotElements Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotElements.html)
[ICWResults::CreateStressHotSpotPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
