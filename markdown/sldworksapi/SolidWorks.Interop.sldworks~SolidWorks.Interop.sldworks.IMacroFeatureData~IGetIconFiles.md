---
title: "IGetIconFiles Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IGetIconFiles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetIconFiles.html"
---

# IGetIconFiles Method (IMacroFeatureData)

Gets the file names for the icons for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetIconFiles( _
   ByVal IconCount As System.Integer, _
   ByRef IconFiles As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim IconCount As System.Integer
Dim IconFiles As System.String

instance.IGetIconFiles(IconCount, IconFiles)
```

### C#

```csharp
void IGetIconFiles(
   System.int IconCount,
   out System.string IconFiles
)
```

### C++/CLI

```cpp
void IGetIconFiles(
   System.int IconCount,
   [Out] System.String^ IconFiles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IconCount`: Number of files for the icons
- `IconFiles`: - in-process, unmanaged C++: Pointer to an array of file names for the icons (see **Remarks)**

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IMacroFeatureData::GetIconFileCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData~GetIconFileCount.html) to determine the size of the array.

The array of the file names for IconFiles can contain either three or nine strings.

| Number of strings in array | Types of images in this order | Image format and sizes |
| --- | --- | --- |
| Three | Regular Suppressed Highlighted | Windows bitmap ( *.bmp ) format 16 pixels wide X 18 pixels high |
| Nine NOTES: This size array is only valid for macro features created in parts, assemblies, and drawings in SOLIDWORKS 2017 and later. SOLIDWORKS displays the appropriate images based on the current DPI setting of the display device. | Regular small Suppressed small Highlighted small Regular medium Suppressed medium Highlighted medium Regular large Suppressed large Highlighted large | Windows bitmap ( *.bmp ) format Recommended sizes are: Small: 20 pixels wide X 20 pixels high Medium: 32 pixels wide X 32 pixels high Large: 40 pixels wide X 40 pixels high |

You can specify either the full path name or just the file name for the strings; for example, c:\bitmaps\icon1.bmp or icon1.bmp.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::ISetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetIconFiles.html)
[IMacroFeatureData::IconFiles Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IconFiles.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
