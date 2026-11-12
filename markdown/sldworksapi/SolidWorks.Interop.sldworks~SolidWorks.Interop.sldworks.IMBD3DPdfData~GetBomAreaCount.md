---
title: "GetBomAreaCount Method (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "GetBomAreaCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetBomAreaCount.html"
---

# GetBomAreaCount Method (IMBD3DPdfData)

Gets the number of BOM Table Areas defined in the [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html) for this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBomAreaCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.Integer

value = instance.GetBomAreaCount()
```

### C#

```csharp
System.int GetBomAreaCount()
```

### C++/CLI

```cpp
System.int GetBomAreaCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of BOM Table Areas defined in the theme

## VBA Syntax

See [MBD3DPdfData::GetBomAreaCount](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~GetBomAreaCount.html).

## Examples

[Export BOM's Second Column to BOM Table Area (C#)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_CSharp.htm)
[Export BOM's Second Column to BOM Table Area (VB.NET)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VBNET.htm)
[Export BOM's Second Column to BOM Table Area (VBA)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VB.htm)

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::SetBomTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetBomTable.html)
[IMBD3DPdfData::ExcludeFromAnnotationView Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ExcludeFromAnnotationView.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
