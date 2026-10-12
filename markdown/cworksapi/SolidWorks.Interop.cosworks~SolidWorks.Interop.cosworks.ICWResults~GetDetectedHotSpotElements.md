---
title: "GetDetectedHotSpotElements Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetDetectedHotSpotElements"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotElements.html"
---

# GetDetectedHotSpotElements Method (ICWResults)

Gets the stress hot spot elements.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDetectedHotSpotElements( _
   ByRef RetVal As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim RetVal As System.Object
Dim value As System.Integer

value = instance.GetDetectedHotSpotElements(RetVal)
```

### C#

```csharp
System.int GetDetectedHotSpotElements(
   out System.object RetVal
)
```

### C++/CLI

```cpp
System.int GetDetectedHotSpotElements(
   [Out] System.Object^ RetVal
)
```

### Parameters

- `RetVal`: Array of stress hot spot elements

### Return Value

1 if successful, 0 if not

## VBA Syntax

See [CWResults::GetDetectedHotSpotElements](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetDetectedHotSpotElements.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

Before calling this method, you must call [ICWResults::RunStressHotSpotDiagnostics](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~RunStressHotSpotDiagnostics.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::CreateStressHotSpotPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html)
[ICWResults::GetDetectedHotSpotNodes Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotNodes.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
