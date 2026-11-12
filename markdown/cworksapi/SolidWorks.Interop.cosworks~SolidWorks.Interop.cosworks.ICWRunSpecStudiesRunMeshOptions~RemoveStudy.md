---
title: "RemoveStudy Method (ICWRunSpecStudiesRunMeshOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRunSpecStudiesRunMeshOptions"
member: "RemoveStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~RemoveStudy.html"
---

# RemoveStudy Method (ICWRunSpecStudiesRunMeshOptions)

Removes the specified study from the run studies batch.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveStudy( _
   ByVal SStudyName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRunSpecStudiesRunMeshOptions
Dim SStudyName As System.String
Dim value As System.Integer

value = instance.RemoveStudy(SStudyName)
```

### C#

```csharp
System.int RemoveStudy(
   System.string SStudyName
)
```

### C++/CLI

```cpp
System.int RemoveStudy(
   System.String^ SStudyName
)
```

### Parameters

- `SStudyName`: Name of study to remove

### Return Value

Error code as defined in [swsRunStudiesRunMeshOptionErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesRunMeshOptionErrorCode_e.html)

## VBA Syntax

See [CWRunSpecStudiesRunMeshOptions::RemoveStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRunSpecStudiesRunMeshOptions~RemoveStudy.html).

## See Also

[ICWRunSpecStudiesRunMeshOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html)
[ICWRunSpecStudiesRunMeshOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
