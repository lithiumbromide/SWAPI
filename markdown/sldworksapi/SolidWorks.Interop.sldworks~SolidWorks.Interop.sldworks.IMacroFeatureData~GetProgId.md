---
title: "GetProgId Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetProgId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProgId.html"
---

# GetProgId Method (IMacroFeatureData)

Gets the version-independent program ID that is valid for this COM feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProgId() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.String

value = instance.GetProgId()
```

### C#

```csharp
System.string GetProgId()
```

### C++/CLI

```cpp
System.String^ GetProgId();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the program ID for the component that implements the COM feature handler

## VBA Syntax

See [MacroFeatureData::GetProgId](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetProgId.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::IsCOMFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IsCOMFeature.html)
[IMacroFeatureData::SetProgId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetProgId.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
