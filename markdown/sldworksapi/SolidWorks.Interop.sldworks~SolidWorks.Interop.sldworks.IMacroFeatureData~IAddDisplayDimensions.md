---
title: "IAddDisplayDimensions Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IAddDisplayDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IAddDisplayDimensions.html"
---

# IAddDisplayDimensions Method (IMacroFeatureData)

Adds the specified display dimensions to this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IAddDisplayDimensions( _
   ByVal DimCount As System.Integer, _
   ByRef DimTypes As System.Integer, _
   ByRef DimValues As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim DimCount As System.Integer
Dim DimTypes As System.Integer
Dim DimValues As System.Double

instance.IAddDisplayDimensions(DimCount, DimTypes, DimValues)
```

### C#

```csharp
void IAddDisplayDimensions(
   System.int DimCount,
   ref System.int DimTypes,
   ref System.double DimValues
)
```

### C++/CLI

```cpp
void IAddDisplayDimensions(
   System.int DimCount,
   System.int% DimTypes,
   System.double% DimValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DimCount`: Number of display dimensions
- `DimTypes`: - in-process, unmanaged C++: Pointer to an array of display dimension types as defined [swDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionType_e.html)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `DimValues`: - in-process, unmanaged C++: Pointer to an array of display dimension values
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
