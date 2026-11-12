---
title: "DuplicateStudy Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "DuplicateStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy.html"
---

# DuplicateStudy Method (ICWStudyManager)

Obsolete. Superseded by [ICWStudyManager::DuplicateStudy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DuplicateStudy( _
   ByVal SName As System.String, _
   ByVal SNewName As System.String, _
   ByVal SConfiguration As System.String, _
   ByVal NNLDynamic As System.Integer, _
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
Dim Errors As System.Integer
Dim value As CWStudy

value = instance.DuplicateStudy(SName, SNewName, SConfiguration, NNLDynamic, Errors)
```

### C#

```csharp
CWStudy DuplicateStudy(
   System.string SName,
   System.string SNewName,
   System.string SConfiguration,
   System.int NNLDynamic,
   out System.int Errors
)
```

### C++/CLI

```cpp
CWStudy^ DuplicateStudy(
   System.String^ SName,
   System.String^ SNewName,
   System.String^ SConfiguration,
   System.int NNLDynamic,
   [Out] System.int Errors
)
```

### Parameters

- `SName`: Name of study to duplicate
- `SNewName`: Name of new study
- `SConfiguration`: Name of configuration
- `NNLDynamic`: 1 to copy to a nonlinear dynamic study, 0 to not
- `Errors`: Error code as defined in [swsDuplicateStudyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsDuplicateStudyError_e.html)

### Return Value

[ICWStudy](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)

## VBA Syntax

See [CWStudyManager::DuplicateStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~DuplicateStudy.html).

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::GetStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~GetStudy.html)
[ICWStudyManager::CreateNewStudy3 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~CreateNewStudy3.html)
[ICWStudyManager::DeleteStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DeleteStudy.html)
[ICWStudyManager::RenameStudyFromID Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RenameStudyFromID.html)
[ICWStudyManager::ConvertStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
