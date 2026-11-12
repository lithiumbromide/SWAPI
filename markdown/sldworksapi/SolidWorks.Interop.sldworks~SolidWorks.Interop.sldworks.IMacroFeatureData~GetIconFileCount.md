---
title: "GetIconFileCount Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetIconFileCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIconFileCount.html"
---

# GetIconFileCount Method (IMacroFeatureData)

Gets the number of the files for the icons for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIconFileCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Integer

value = instance.GetIconFileCount()
```

### C#

```csharp
System.int GetIconFileCount()
```

### C++/CLI

```cpp
System.int GetIconFileCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of files for the icons

## VBA Syntax

See [MacroFeatureData::GetIconFileCount](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetIconFileCount.html).

## Remarks

Call this method before calling [IMacroFeatureData::IGetIconFiles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetIconFiles.html) to determine the size of the array for that method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::IGetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetIconFiles.html)
[IMacroFeatureData::ISetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetIconFiles.html)
[IMacroFeatureData::IconFiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IconFiles.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
