---
title: "ThemeName Property (IMBD3DPdfData)"
project: "SOLIDWORKS API Help"
interface: "IMBD3DPdfData"
member: "ThemeName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.html"
---

# ThemeName Property (IMBD3DPdfData)

Gets or sets the path and file name of the theme for this SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThemeName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMBD3DPdfData
Dim value As System.String

instance.ThemeName = value

value = instance.ThemeName
```

### C#

```csharp
System.string ThemeName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ThemeName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name of the theme

## VBA Syntax

See [MBD3DPdfData::ThemeName](ms-its:sldworksapivb6.chm::/sldworks~MBD3DPdfData~ThemeName.html).

## Examples

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

## Remarks

You can also get or set the SOLIDWORKS MBD 3D PDF path for a theme using:

- SOLIDWORKS API. Call:

  - [ISldWorks::GetUserPreferenceStringValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html)(swUserPreferenceStringValue_e.swFileLocationsThemeFolder) or
  - [ISldWorks::SetUserPreferenceStringValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.html)(swUserPreferenceStringValue_e.swFileLocationsThemeFolder, <V`alue`>)
- SOLIDWORKS Design user interface. Click **Tools > System Options > File Locations > 3D PDF Themes** in **Show folders for**.

## See Also

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html)
[IMBD3DPdfData::SetIndependentViewPort Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetIndependentViewPort.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
