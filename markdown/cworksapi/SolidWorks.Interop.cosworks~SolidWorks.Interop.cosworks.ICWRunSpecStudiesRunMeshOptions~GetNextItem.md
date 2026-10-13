---
title: "GetNextItem Method (ICWRunSpecStudiesRunMeshOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRunSpecStudiesRunMeshOptions"
member: "GetNextItem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~GetNextItem.html"
---

# GetNextItem Method (ICWRunSpecStudiesRunMeshOptions)

Gets the next item in the run studies batch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextItem( _
   ByRef SStudyName As System.String, _
   ByRef NRunMeshOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRunSpecStudiesRunMeshOptions
Dim SStudyName As System.String
Dim NRunMeshOption As System.Integer
Dim value As System.Integer

value = instance.GetNextItem(SStudyName, NRunMeshOption)
```

### C#

```csharp
System.int GetNextItem(
   out System.string SStudyName,
   out System.int NRunMeshOption
)
```

### C++/CLI

```cpp
System.int GetNextItem(
   [Out] System.String^ SStudyName,
   [Out] System.int NRunMeshOption
)
```

### Parameters

- `SStudyName`: Name of study
- `NRunMeshOption`: Run and mesh option as defined in [swsRunStudiesRunMeshOptions_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesRunMeshOptions_e.html)

### Return Value

Error code as defined in [swsRunStudiesRunMeshOptionErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesRunMeshOptionErrorCode_e.html)

## VBA Syntax

See [CWRunSpecStudiesRunMeshOptions::GetNextItem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRunSpecStudiesRunMeshOptions~GetNextItem.html).

## See Also

[ICWRunSpecStudiesRunMeshOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html)
[ICWRunSpecStudiesRunMeshOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions_members.html)
[ICWRunSpecStudiesRunMeshOptions::GetFirstItem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~GetFirstItem.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
