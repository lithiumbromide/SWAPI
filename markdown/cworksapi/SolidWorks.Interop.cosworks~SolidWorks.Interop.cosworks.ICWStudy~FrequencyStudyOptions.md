---
title: "FrequencyStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "FrequencyStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~FrequencyStudyOptions.html"
---

# FrequencyStudyOptions Property (ICWStudy)

Gets the options for this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FrequencyStudyOptions As CWFrequencyStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWFrequencyStudyOptions

value = instance.FrequencyStudyOptions
```

### C#

```csharp
CWFrequencyStudyOptions FrequencyStudyOptions {get;}
```

### C++/CLI

```cpp
property CWFrequencyStudyOptions^ FrequencyStudyOptions {
   CWFrequencyStudyOptions^ get();
}
```

### Property Value

[Frequency study options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWFrequencyStudyOptions.html)

## VBA Syntax

See [CWStudy::FrequencyStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~FrequencyStudyOptions.html).

## Examples

[Create Frequency Study with Solid Mesh (VBA)](Create_Frequency_Study_with_Solid_Mesh_Example_VB.htm)
[Create Frequency Study with Solid Mesh (VB.NET)](Create_Frequency_Study_with_Solid_Mesh_Example_VBNET.htm)
[Create Frequency Study with Solid Mesh (C#)](Create_Frequency_Study_with_Solid_Mesh_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
