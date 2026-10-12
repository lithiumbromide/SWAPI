---
title: "GetFirstItem Method (ICWRunStudiesResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRunStudiesResults"
member: "GetFirstItem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults~GetFirstItem.html"
---

# GetFirstItem Method (ICWRunStudiesResults)

Gets the first study and result code in the run studies batch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstItem( _
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

value = instance.GetFirstItem(SStudyName, NRunStatus)
```

### C#

```csharp
System.int GetFirstItem(
   out System.string SStudyName,
   out System.int NRunStatus
)
```

### C++/CLI

```cpp
System.int GetFirstItem(
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

See [CWRunStudiesResults::GetFirstItem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRunStudiesResults~GetFirstItem.html).

## Examples

See the [ICWRunStudiesResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html) examples.

## See Also

[ICWRunStudiesResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html)
[ICWRunStudiesResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults_members.html)
[ICWRunStudiesResults::GetNextItem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults~GetNextItem.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
