---
title: "ReplaceOption Method (ICWRunSpecStudiesRunMeshOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRunSpecStudiesRunMeshOptions"
member: "ReplaceOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~ReplaceOption.html"
---

# ReplaceOption Method (ICWRunSpecStudiesRunMeshOptions)

Replaces the run and mesh option of the specified study with a new option.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceOption( _
   ByVal SStudyName As System.String, _
   ByVal NRunMeshOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRunSpecStudiesRunMeshOptions
Dim SStudyName As System.String
Dim NRunMeshOption As System.Integer
Dim value As System.Integer

value = instance.ReplaceOption(SStudyName, NRunMeshOption)
```

### C#

```csharp
System.int ReplaceOption(
   System.string SStudyName,
   System.int NRunMeshOption
)
```

### C++/CLI

```cpp
System.int ReplaceOption(
   System.String^ SStudyName,
   System.int NRunMeshOption
)
```

### Parameters

- `SStudyName`: Name of study
- `NRunMeshOption`: New run and mesh option as defined in [swsRunStudiesRunMeshOptions_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesRunMeshOptions_e.html)

### Return Value

Error code as defined in [swsRunStudiesRunMeshOptionErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesRunMeshOptionErrorCode_e.html)

## VBA Syntax

See [CWRunSpecStudiesRunMeshOptions::ReplaceOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRunSpecStudiesRunMeshOptions~ReplaceOption.html).

## See Also

[ICWRunSpecStudiesRunMeshOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html)
[ICWRunSpecStudiesRunMeshOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions_members.html)
[ICWRunSpecStudiesRunMeshOptions::RemoveAll Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~RemoveAll.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
