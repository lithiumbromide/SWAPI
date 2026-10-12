---
title: "InsertDwgOrDxfFile2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertDwgOrDxfFile2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.html"
---

# InsertDwgOrDxfFile2 Method (IFeatureManager)

Inserts a DXF/DWG image feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDwgOrDxfFile2( _
   ByVal FileName As System.String, _
   ByVal DxfDwgImportData As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FileName As System.String
Dim DxfDwgImportData As System.Object
Dim value As Feature

value = instance.InsertDwgOrDxfFile2(FileName, DxfDwgImportData)
```

### C#

```csharp
Feature InsertDwgOrDxfFile2(
   System.string FileName,
   System.object DxfDwgImportData
)
```

### C++/CLI

```cpp
Feature^ InsertDwgOrDxfFile2(
   System.String^ FileName,
   System.Object^ DxfDwgImportData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the DXF/DWG image file
- `DxfDwgImportData`: [IImportDxfDwgData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData.html)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertDwgOrDxfFile2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertDwgOrDxfFile2.html).

## Examples

[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)

## Remarks

Before calling this method, select a plane or planar surface on which to place the image.

This method:

- returns Nothing or null if the file contains solid bodies data.
- is not supported for use in assembly documents.

When importing DXF/DWG data, you can:

- Let SOLIDWORKS determine the default values:
- - Paper size and sheet scale are computed to fit the input data.
  - Length unit is determined from the header of the input DXF/DWG file.
  - Sheet name is the same as the layout name in the input DXF/DWG file.

- or -

- Set your own values:

  1. Call [ISldWorks::GetImportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetImportFileData.html) to obtain the IImportDxfDwgData interface.
  2. Use the following methods with a Sheet argument of "" (an empty string), to set up your defaults:

    - [IImportDxfDwgData::GetPaperSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~GetPaperSize.html)
    - [IImportDxfDwgData::GetPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~GetPosition.html)
    - [IImportDxfDwgData::GetSheetScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~GetSheetScale.html)
    - [IImportDxfDwgData::ImportMethod](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~ImportMethod.html)
    - [IImportDxfDwgData::LengthUnit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~LengthUnit.html)
    - [IImportDxfDwgData::SetPaperSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~SetPaperSize.html)
    - [IImportDxfDwgData::SetPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~SetPosition.html)
    - [IImportDxfDwgData::SetSheetScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~SetSheetScale.html)
    - [IImportDxfDwgData::SheetName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData~SheetName.html)

NOTES:

- Getting the IImportDxfDwgData interface does not get default values from the input file. Any values not set by you are set to the values computed by SOLIDWORKS.
- If the DWG/DXF file has multiple sheets, use these methods with a valid layout name in the Sheet argument to set up sheet specific settings, which override the default settings. If any of the individual items are not specified for a given layout name, then the value used is from the defaults (layout name ""). If the default value is not specified, then SOLIDWORKS computes and uses a meaningful value for that item.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
