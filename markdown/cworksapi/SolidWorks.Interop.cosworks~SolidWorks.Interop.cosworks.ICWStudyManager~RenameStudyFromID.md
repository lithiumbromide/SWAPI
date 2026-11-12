---
title: "RenameStudyFromID Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "RenameStudyFromID"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RenameStudyFromID.html"
---

# RenameStudyFromID Method (ICWStudyManager)

Renames the study that has the specified ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function RenameStudyFromID( _
   ByVal NIndex As System.Integer, _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim NIndex As System.Integer
Dim SName As System.String
Dim value As System.Integer

value = instance.RenameStudyFromID(NIndex, SName)
```

### C#

```csharp
System.int RenameStudyFromID(
   System.int NIndex,
   System.string SName
)
```

### C++/CLI

```cpp
System.int RenameStudyFromID(
   System.int NIndex,
   System.String^ SName
)
```

### Parameters

- `NIndex`: ID of study to rename
- `SName`: New name of study

### Return Value

Error as defined by [swsStudyError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStudyError_e.html)

## VBA Syntax

See [CWStudyManager::RenameStudyFromID](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~RenameStudyFromID.html).

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::RenameStudyFromName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~RenameStudyFromName.html)
[ICWStudyManager::DuplicateStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy.html)
[ICWStudyManager::ConvertStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
