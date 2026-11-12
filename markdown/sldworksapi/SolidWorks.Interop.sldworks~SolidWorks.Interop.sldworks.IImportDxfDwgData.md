---
title: "IImportDxfDwgData Interface"
project: "SOLIDWORKS API Help"
interface: "IImportDxfDwgData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html"
---

# IImportDxfDwgData Interface

Allows you to specify values when importing or inserting DXF/DWG data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IImportDxfDwgData
```

### Visual Basic (Usage)

```vb
Dim instance As IImportDxfDwgData
```

### C#

```csharp
public interface IImportDxfDwgData
```

### C++/CLI

```cpp
public interface class IImportDxfDwgData
```

## VBA Syntax

See [ImportDxfDwgData](ms-its:sldworksapivb6.chm::/sldworks~ImportDxfDwgData.html).

## Examples

[Import DXF File into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)
[Import DXF File into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)

## Remarks

When importing DXF/DWG data, you can:

- Let SOLIDWORKS determine the default values:

  - Paper size and sheet scale are computed to fit the input data.
  - Length unit is determined from the header of the input DXF/DWG file.
  - Sheet name is the same as the layout name in the input DXF/DWG file.

- or -

- Set your own values by using:

  1. [ISldWorks::GetImportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetImportFileData.html) to obtain the IImportDxfDwgData interface.
  2. Use the following methods with a Sheet argument of "" (an empty string), to set up your defaults before importing or inserting the file:

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
- If the DWG/DXF file has multiple sheets, use these methods with a valid layout name in the Sheet argument to set up sheet specific settings, which override the default settings. If any of the individual items are not specified for a given layout name, the value used is from the defaults (layout name ""). If the default value is not specified, SOLIDWORKS computes and uses a meaningful value for that item.

When inserting DXF/DWG data as a feature into the current model document, first select a plane or planar surface and then call [IFeatureManager::InsertDwgOrDxfFile2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.html).

Call [ISldWorks::LoadFile4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadFile4.html) to import the DXF/DWG file as a new SOLIDWORKS model document.

## Accessors

[ISldWorks::GetImportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetImportFileData.html)

## Access Diagram

[ImportDxfDwgData](SWObjectModel.pdf#ImportDxfDwgData)

## See Also

[IImportDxfDwgData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IImportIgesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html)
