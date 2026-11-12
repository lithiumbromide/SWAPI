---
title: "RunSpecifiedStudyByName Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "RunSpecifiedStudyByName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RunSpecifiedStudyByName.html"
---

# RunSpecifiedStudyByName Method (ICWStudyManager)

Runs specified studies in batch mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunSpecifiedStudyByName( _
   ByRef ErrorCode As System.Integer _
) As CWRunStudiesResults
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim ErrorCode As System.Integer
Dim value As CWRunStudiesResults

value = instance.RunSpecifiedStudyByName(ErrorCode)
```

### C#

```csharp
CWRunStudiesResults RunSpecifiedStudyByName(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRunStudiesResults^ RunSpecifiedStudyByName(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsRunStudiesErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesErrorCode_e.html)

### Return Value

[ICWRunStudiesResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html)

## VBA Syntax

See [CWStudyManager::RunSpecifiedStudyByName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~RunSpecifiedStudyByName.html).

## Examples

[Run Studies in Batch Mode (VBA)](Run_Studies_in_Batch_Mode_Example_VB.htm)
[Run Studies in Batch Mode (VB.NET)](Run_Studies_in_Batch_Mode_Example_VBNET.htm)
[Run Studies in Batch Mode (C#)](Run_Studies_in_Batch_Mode_Example_CSharp.htm)

## Remarks

Before calling this method, set the run and mesh options for the study using [ICWStudyManager::RunSpecifiedStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RunSpecifiedStudyOptions.html).

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::RunAllStudies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RunAllStudies.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
