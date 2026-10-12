---
title: "GetImportFileData Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetImportFileData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetImportFileData.html"
---

# GetImportFileData Method (ISldWorks)

Gets the IGES or DXF/DWG import data for the specified file.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetImportFileData( _
   ByVal FileName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object

value = instance.GetImportFileData(FileName)
```

### C#

```csharp
System.object GetImportFileData(
   System.string FileName
)
```

### C++/CLI

```cpp
System.Object^ GetImportFileData(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and name of the IGES or DXF/DWG file

### Return Value

[IGES import data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportIgesData.html) or [DXF/DWG import data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IImportDxfDwgData.html)

## VBA Syntax

See [SldWorks::GetImportFileData](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetImportFileData.html).

## Examples

[Import DXF File Into Part Sketch (VBA)](Import_DXF_File_into_Part_Sketch_Example_VB.htm)
[Import DXF File Into Drawing (VBA)](Import_DXF_File_to_Drawing_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Insert DXF/DWG File and Add Dimensions (VB.NET)](Insert_DXF_File_and_Add_Dimensions_Example_VBNET.htm)
[Insert DXF/DWG File and Add Dimensions (C#)](Insert_DXF_File_and_Add_Dimensions_Example_CSharp.htm)
[Insert and Position DXF/DWG File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)
[Insert and Position DXF/DWG File in Drawing (VB.NET)](Insert_and_Position_DXF_File_in_Drawing_Example_VBNET.htm)
[Insert and Position DXF/DWG File in Drawing (C#)](Insert_and_Position_DXF_File_in_Drawing_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

## Remarks

Getting the interface object does not retrieve any information from the input file or set up defaults at this time. Instead, it sets up information such that when it is used in the import process, SOLIDWORKS will compute defaults on the fly.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::LoadFile4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[IFeatureManager::InsertDwgOrDxfFile2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.html)

## Availability

SOLIDWORKS 2005 SP3, Revision Number 13.3
