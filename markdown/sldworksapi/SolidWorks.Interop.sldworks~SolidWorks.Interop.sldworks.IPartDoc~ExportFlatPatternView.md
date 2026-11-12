---
title: "ExportFlatPatternView Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ExportFlatPatternView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportFlatPatternView.html"
---

# ExportFlatPatternView Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::ExportToDWG2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportToDWG2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportFlatPatternView( _
   ByVal FilePath As System.String, _
   ByVal Options As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim FilePath As System.String
Dim Options As System.Integer
Dim value As System.Boolean

value = instance.ExportFlatPatternView(FilePath, Options)
```

### C#

```csharp
System.bool ExportFlatPatternView(
   System.string FilePath,
   System.int Options
)
```

### C++/CLI

```cpp
System.bool ExportFlatPatternView(
   System.String^ FilePath,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePath`: Path and filename to which to save the sheet metal part in its flattened state to a DXF/DWG file
- `Options`: Option as described in [swExportFlatPatternViewOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportFlatPatternViewOptions_e.html)

### Return Value

True if the sheet metal part is enabled to be saved in its flattened state to a DXF/DWG file at the specified path and filename, false if not

## VBA Syntax

See [PartDoc::ExportFlatPatternView](ms-its:sldworksapivb6.chm::/Sldworks~PartDoc~ExportFlatPatternView.html).

## Examples

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long

Sub main()
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension

boolstatus = swModel.ExportFlatPatternView("F:\Test\Flat pattern - sheet_metal_cover.DXF", swExportFlatPatternOption_None)
swModelDocExt.SaveAs "F:\Test\Flat pattern - sheet_metal_cover.DXF", 0, 0, Nothing, longstatus, longwarnings

End Sub
```

## Remarks

Call this method before calling [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ExportToDWG2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ExportToDWG2.html)
[IPartDoc::IExportToDWG2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IExportToDWG2.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
