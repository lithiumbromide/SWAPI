---
title: "SetResultFolderPath2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetResultFolderPath2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetResultFolderPath2.html"
---

# SetResultFolderPath2 Method (ICWDynamicStudyOptions)

Sets the path to the folder that stores the results of this dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetResultFolderPath2( _
   ByVal SResultFolderPath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim SResultFolderPath As System.String
Dim value As System.Integer

value = instance.SetResultFolderPath2(SResultFolderPath)
```

### C#

```csharp
System.int SetResultFolderPath2(
   System.string SResultFolderPath
)
```

### C++/CLI

```cpp
System.int SetResultFolderPath2(
   System.String^ SResultFolderPath
)
```

### Parameters

- `SResultFolderPath`: Path to the results folder

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetResultFolderPath2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetResultFolderPath2.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetResultFolderPath2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetResultFolderPath2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
