---
title: "DuplicateStudy2 Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "DuplicateStudy2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy2.html"
---

# DuplicateStudy2 Method (ICWStudyManager)

Duplicates the specified study.

## Syntax

### Visual Basic (Declaration)

```vb
Function DuplicateStudy2( _
   ByVal SName As System.String, _
   ByVal SNewName As System.String, _
   ByVal SConfiguration As System.String, _
   ByVal NNLDynamic As System.Integer, _
   ByVal BIncludeMesh As System.Boolean, _
   ByVal BIncludeResults As System.Boolean, _
   ByRef Errors As System.Integer _
) As CWStudy
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim SName As System.String
Dim SNewName As System.String
Dim SConfiguration As System.String
Dim NNLDynamic As System.Integer
Dim BIncludeMesh As System.Boolean
Dim BIncludeResults As System.Boolean
Dim Errors As System.Integer
Dim value As CWStudy

value = instance.DuplicateStudy2(SName, SNewName, SConfiguration, NNLDynamic, BIncludeMesh, BIncludeResults, Errors)
```

### C#

```csharp
CWStudy DuplicateStudy2(
   System.string SName,
   System.string SNewName,
   System.string SConfiguration,
   System.int NNLDynamic,
   System.bool BIncludeMesh,
   System.bool BIncludeResults,
   out System.int Errors
)
```

### C++/CLI

```cpp
CWStudy^ DuplicateStudy2(
   System.String^ SName,
   System.String^ SNewName,
   System.String^ SConfiguration,
   System.int NNLDynamic,
   System.bool BIncludeMesh,
   System.bool BIncludeResults,
   [Out] System.int Errors
)
```

### Parameters

- `SName`: Name of study to duplicate
- `SNewName`: Name of new study
- `SConfiguration`: Name of configuration
- `NNLDynamic`: 1 to copy to a nonlinear dynamic study, 0 to not
- `BIncludeMesh`: True to include mesh when duplicating study, false to not
- `BIncludeResults`: True to include results when duplicating study, false to not
- `Errors`: Error code as defined in [swsDuplicateStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDuplicateStudyError_e.html)

### Return Value

[ICWStudy](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)

## VBA Syntax

See [CWStudyManager::DuplicateStudy2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~DuplicateStudy2.html).

## Examples

[Duplicate Study (VBA)](Duplicate_Study_Example_VB.htm)
[Duplicate Study (VB.NET)](Duplicate_Study_Example_VBNET.htm)
[Duplicate Study (C#)](Duplicate_Study_Example_CSharp.htm)

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::GetStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~GetStudy.html)
[ICWStudyManager::CreateNewStudy3 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~CreateNewStudy3.html)
[ICWStudyManager::DeleteStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DeleteStudy.html)
[ICWStudyManager::RenameStudyFromID Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RenameStudyFromID.html)
[ICWStudyManager::ConvertStudy2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy2.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
