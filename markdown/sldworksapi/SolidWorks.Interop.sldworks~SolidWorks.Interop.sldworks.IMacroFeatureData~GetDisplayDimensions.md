---
title: "GetDisplayDimensions Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "GetDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.html"
---

# GetDisplayDimensions Method (IMacroFeatureData)

Gets the display dimensions for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimensions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Object

value = instance.GetDisplayDimensions()
```

### C#

```csharp
System.object GetDisplayDimensions()
```

### C++/CLI

```cpp
System.Object^ GetDisplayDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [display dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [MacroFeatureData::GetDisplayDimensions](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~GetDisplayDimensions.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::IGetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetDisplayDimensions.html)
[IMacroFeatureData::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
