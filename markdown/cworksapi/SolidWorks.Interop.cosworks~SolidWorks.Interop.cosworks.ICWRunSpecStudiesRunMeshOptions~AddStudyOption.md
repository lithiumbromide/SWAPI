---
title: "AddStudyOption Method (ICWRunSpecStudiesRunMeshOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRunSpecStudiesRunMeshOptions"
member: "AddStudyOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions~AddStudyOption.html"
---

# AddStudyOption Method (ICWRunSpecStudiesRunMeshOptions)

Adds the specified run and mesh option to the specified study.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddStudyOption( _
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

value = instance.AddStudyOption(SStudyName, NRunMeshOption)
```

### C#

```csharp
System.int AddStudyOption(
   System.string SStudyName,
   System.int NRunMeshOption
)
```

### C++/CLI

```cpp
System.int AddStudyOption(
   System.String^ SStudyName,
   System.int NRunMeshOption
)
```

### Parameters

- `SStudyName`: Name of study
- `NRunMeshOption`: Run and mesh option as defined in [swsRunStudiesRunMeshOptions_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesRunMeshOptions_e.html)

### Return Value

Error code as defined in [swsRunStudiesRunMeshOptionErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesRunMeshOptionErrorCode_e.html)

## VBA Syntax

See [CWRunSpecStudiesRunMeshOptions::AddStudyOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRunSpecStudiesRunMeshOptions~AddStudyOption.html).

## Examples

See the [ICWRunSpecStudiesRunMeshOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html) examples.

## See Also

[ICWRunSpecStudiesRunMeshOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html)
[ICWRunSpecStudiesRunMeshOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
