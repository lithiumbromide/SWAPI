---
title: "DeleteStudy Method (ICWStudyManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyManager"
member: "DeleteStudy"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DeleteStudy.html"
---

# DeleteStudy Method (ICWStudyManager)

Deletes the specified study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteStudy( _
   ByVal StudyName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyManager
Dim StudyName As System.String

instance.DeleteStudy(StudyName)
```

### C#

```csharp
void DeleteStudy(
   System.string StudyName
)
```

### C++/CLI

```cpp
void DeleteStudy(
   System.String^ StudyName
)
```

### Parameters

- `StudyName`: Study name

## VBA Syntax

See [CWStudyManager::DeleteStudy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyManager~DeleteStudy.html).

## Examples

[Calculate Edge Weld Results (C#)](Calculate_Edge_Weld_Results_Example_CSharp.htm)
[Calculate Edge Weld Results (VB.NET)](Calculate_Edge_Weld_Results_Example_VBNET.htm)
[Calculate Edge Weld Results (VBA)](Calculate_Edge_Weld_Results_Example_VB.htm)

## See Also

[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
[ICWStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager_members.html)
[ICWStudy::Name Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~Name.html)
[ICWModelDoc::DuplicateStudy Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~DuplicateStudy.html)
[ICWStudyManager::ConvertStudy Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager~ConvertStudy.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
