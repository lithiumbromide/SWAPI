---
title: "GetFirstItem Method (ICWRunSpecStudiesRunMeshOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRunSpecStudiesRunMeshOptions"
member: "GetFirstItem"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~GetFirstItem.html"
---

# GetFirstItem Method (ICWRunSpecStudiesRunMeshOptions)

Gets the first item in the run studies batch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstItem( _
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

value = instance.GetFirstItem(SStudyName, NRunMeshOption)
```

### C#

```csharp
System.int GetFirstItem(
   out System.string SStudyName,
   out System.int NRunMeshOption
)
```

### C++/CLI

```cpp
System.int GetFirstItem(
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

See [CWRunSpecStudiesRunMeshOptions::GetFirstItem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRunSpecStudiesRunMeshOptions~GetFirstItem.html).

## See Also

[ICWRunSpecStudiesRunMeshOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html)
[ICWRunSpecStudiesRunMeshOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions_members.html)
[ICWRunSpecStudiesRunMeshOptions::GetNextItem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~GetNextItem.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
