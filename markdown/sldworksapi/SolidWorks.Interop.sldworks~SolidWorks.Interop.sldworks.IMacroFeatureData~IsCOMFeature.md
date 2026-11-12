---
title: "IsCOMFeature Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IsCOMFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IsCOMFeature.html"
---

# IsCOMFeature Method (IMacroFeatureData)

Gets whether the feature is a COM feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCOMFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Boolean

value = instance.IsCOMFeature()
```

### C#

```csharp
System.bool IsCOMFeature()
```

### C++/CLI

```cpp
System.bool IsCOMFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the feature is a COM feature, false if not

## VBA Syntax

See [MacroFeatureData::IsCOMFeature](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~IsCOMFeature.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetProgId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProgId.html)
[IMacroFeatureData::SetProgId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetProgId.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
