---
title: "RunAllStudies Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "RunAllStudies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RunAllStudies.html"
---

# RunAllStudies Method (ICWStudyManager)

Runs all studies in batch mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunAllStudies( _
   ByRef ErrorCode As System.Integer _
) As CWRunStudiesResults
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim ErrorCode As System.Integer
Dim value As CWRunStudiesResults

value = instance.RunAllStudies(ErrorCode)
```

### C#

```csharp
CWRunStudiesResults RunAllStudies(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRunStudiesResults^ RunAllStudies(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsRunStudiesErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStudiesErrorCode_e.html)

### Return Value

[ICWRunStudiesResults](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRunStudiesResults.html)

## VBA Syntax

See [CWStudyManager::RunAllStudies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~RunAllStudies.html).

## Remarks

Before calling this method, set the run and mesh options for the studies using [ICWStudyManager::RunSpecifiedStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RunSpecifiedStudyOptions.html).

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::RunSpecifiedStudyByName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RunSpecifiedStudyByName.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
