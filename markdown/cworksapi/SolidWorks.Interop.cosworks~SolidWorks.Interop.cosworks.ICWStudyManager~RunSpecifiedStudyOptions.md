---
title: "RunSpecifiedStudyOptions Property (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "RunSpecifiedStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RunSpecifiedStudyOptions.html"
---

# RunSpecifiedStudyOptions Property (ICWStudyManager)

Gets the run and mesh option for studies run in batch mode.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RunSpecifiedStudyOptions As CWRunSpecStudiesRunMeshOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim value As CWRunSpecStudiesRunMeshOptions

value = instance.RunSpecifiedStudyOptions
```

### C#

```csharp
CWRunSpecStudiesRunMeshOptions RunSpecifiedStudyOptions {get;}
```

### C++/CLI

```cpp
property CWRunSpecStudiesRunMeshOptions^ RunSpecifiedStudyOptions {
   CWRunSpecStudiesRunMeshOptions^ get();
}
```

### Property Value

[ICWRunSpecStudiesRunMeshOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunSpecStudiesRunMeshOptions.html)

## VBA Syntax

See [CWStudyManager::RunSpecifiedStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~RunSpecifiedStudyOptions.html).

## Examples

[Run Studies in Batch Mode (VBA)](Run_Studies_in_Batch_Mode_Example_VB.htm)
[Run Studies in Batch Mode (VB.NET)](Run_Studies_in_Batch_Mode_Example_VBNET.htm)
[Run Studies in Batch Mode (C#)](Run_Studies_in_Batch_Mode_Example_CSharp.htm)

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
