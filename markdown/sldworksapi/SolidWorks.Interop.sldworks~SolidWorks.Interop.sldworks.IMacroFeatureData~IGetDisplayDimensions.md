---
title: "IGetDisplayDimensions Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetDisplayDimensions.html"
---

# IGetDisplayDimensions Method (IMacroFeatureData)

Gets the display dimensions for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetDisplayDimensions( _
   ByVal DimCount As System.Integer, _
   ByRef Dims As DisplayDimension _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim DimCount As System.Integer
Dim Dims As DisplayDimension

instance.IGetDisplayDimensions(DimCount, Dims)
```

### C#

```csharp
void IGetDisplayDimensions(
   System.int DimCount,
   out DisplayDimension Dims
)
```

### C++/CLI

```cpp
void IGetDisplayDimensions(
   System.int DimCount,
   [Out] DisplayDimension^ Dims
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DimCount`: Number of display dimensions
- `Dims`: - in-process, unmanaged C++: Pointer to an array of [display dimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMacroFeatureData::GetDisplayDimensionCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetDisplayDimensionCount.html) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetDisplayDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetDisplayDimensions.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
