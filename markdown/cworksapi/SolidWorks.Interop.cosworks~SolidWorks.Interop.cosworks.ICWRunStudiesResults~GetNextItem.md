---
title: "GetNextItem Method (ICWRunStudiesResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRunStudiesResults"
member: "GetNextItem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults~GetNextItem.html"
---

# GetNextItem Method (ICWRunStudiesResults)

Gets the next study and result code in the run studies batch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextItem( _
   ByRef SStudyName As System.String, _
   ByRef NRunStatus As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRunStudiesResults
Dim SStudyName As System.String
Dim NRunStatus As System.Integer
Dim value As System.Integer

value = instance.GetNextItem(SStudyName, NRunStatus)
```

### C#

```csharp
System.int GetNextItem(
   out System.string SStudyName,
   out System.int NRunStatus
)
```

### C++/CLI

```cpp
System.int GetNextItem(
   [Out] System.String^ SStudyName,
   [Out] System.int NRunStatus
)
```

### Parameters

- `SStudyName`: Name of study
- `NRunStatus`: Error code of SStudyName as defined in [swsRunStudiesStatusCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesStatusCode_e.html)

### Return Value

Error code as defined in [swsRunStudiesResultsErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesResultsErrorCode_e.html)

## VBA Syntax

See [CWRunStudiesResults::GetNextItem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRunStudiesResults~GetNextItem.html).

## Examples

See the [ICWRunStudiesResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html) examples.

## See Also

[ICWRunStudiesResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html)
[ICWRunStudiesResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults_members.html)
[ICWRunStudiesResults::GetFirstItem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults~GetFirstItem.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
