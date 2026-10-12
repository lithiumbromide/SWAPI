---
title: "IconFiles Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "IconFiles"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IconFiles.html"
---

# IconFiles Property (IMacroFeatureData)

Gets or sets the file names for the icons for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IconFiles As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.Object

instance.IconFiles = value

value = instance.IconFiles
```

### C#

```csharp
System.object IconFiles {get; set;}
```

### C++/CLI

```cpp
property System.Object^ IconFiles {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of the file names for the icons (see **Remarks**)

## VBA Syntax

See [MacroFeatureData::IconFiles](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~IconFiles.html).

## Remarks

The array of the file names for the icons can contain either three or nine strings.

| Number of strings in array | Types of images in this order | Image format and sizes |
| --- | --- | --- |
| Three | Regular Suppressed Highlighted | Windows bitmap ( *.bmp ) format 16 pixels wide X 18 pixels high |
| Nine NOTES: This size array is only valid for macro features created in parts, assemblies, and drawings in SOLIDWORKS 2017 and later. SOLIDWORKS displays the appropriate images based on the current DPI setting of the display device. | Regular small Suppressed small Highlighted small Regular medium Suppressed medium Highlighted medium Regular large Suppressed large Highlighted large | Windows bitmap ( *.bmp ) format Recommended sizes are: Small: 20 pixels wide X 20 pixels high Medium: 32 pixels wide X 32 pixels high Large: 40 pixels wide X 40 pixels high |

You can specify either the full path name or just the file name for the strings; for example, c:\bitmaps\icon1.bmp or icon1.bmp.

If you change the bitmaps after inserting them with a macro feature into a SOLIDWORKS document, then the new bitmaps are not displayed until you exit and restart SOLIDWORKS.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetIconFileCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetIconFileCount.html)
[IMacroFeatureData::IGetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetIconFiles.html)
[IMacroFeatureData::ISetIconFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetIconFiles.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
