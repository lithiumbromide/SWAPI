---
title: "GetResultFolderPath2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetResultFolderPath2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResultFolderPath2.html"
---

# GetResultFolderPath2 Method (ICWDynamicStudyOptions)

Gets the path to the folder that stores the results of this dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResultFolderPath2( _
   ByRef SResultFolderPath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim SResultFolderPath As System.String
Dim value As System.Integer

value = instance.GetResultFolderPath2(SResultFolderPath)
```

### C#

```csharp
System.int GetResultFolderPath2(
   out System.string SResultFolderPath
)
```

### C++/CLI

```cpp
System.int GetResultFolderPath2(
   [Out] System.String^ SResultFolderPath
)
```

### Parameters

- `SResultFolderPath`: Path to the results folder

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetResultFolderPath2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetResultFolderPath2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetResultFolderPath2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResultFolderPath2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
