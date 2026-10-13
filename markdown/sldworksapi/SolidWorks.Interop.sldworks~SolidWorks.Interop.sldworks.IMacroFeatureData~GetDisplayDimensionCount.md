---
title: "GetDisplayDimensionCount Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetDisplayDimensionCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensionCount.html"
---

# GetDisplayDimensionCount Method (IMacroFeatureData)

Gets the number of display dimensions for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimensionCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Integer

value = instance.GetDisplayDimensionCount()
```

### C#

```csharp
System.int GetDisplayDimensionCount()
```

### C++/CLI

```cpp
System.int GetDisplayDimensionCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of display dimensions

## VBA Syntax

See [MacroFeatureData::GetDisplayDimensionCount](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetDisplayDimensionCount.html).

## Remarks

Call this method before calling [IMacroFeatureData::IGetDisplayDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~IGetDisplayDimensions.html) to determine the size of the array for that method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
