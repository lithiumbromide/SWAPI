---
title: "StudyCount Property (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "StudyCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~StudyCount.html"
---

# StudyCount Property (ICWStudyManager)

Gets the number of studies in the open document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StudyCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim value As System.Integer

value = instance.StudyCount
```

### C#

```csharp
System.int StudyCount {get;}
```

### C++/CLI

```cpp
property System.int StudyCount {
   System.int get();
}
```

### Property Value

Number of studies

## VBA Syntax

See [CWStudyManager::StudyCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~StudyCount.html).

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudyManager::GetStudy Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~GetStudy.html)
[ICWStudyManager::ActiveStudy Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ActiveStudy.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
