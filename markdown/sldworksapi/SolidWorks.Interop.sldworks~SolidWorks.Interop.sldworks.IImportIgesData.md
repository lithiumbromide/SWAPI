---
title: "IImportIgesData Interface"
project: "SOLIDWORKS API Help"
interface: "IImportIgesData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData.html"
---

# IImportIgesData Interface

Allows you to specify levels and values when importing IGES data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IImportIgesData
```

### Visual Basic (Usage)

```vb
Dim instance As IImportIgesData
```

### C#

```csharp
public interface IImportIgesData
```

### C++/CLI

```cpp
public interface class IImportIgesData
```

## VBA Syntax

See [ImportIgesData](ms-its:sldworksapivb6.chm::/sldworks~ImportIgesData.html).

## Examples

[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

## Remarks

| If user preference swIGESImportShowLevel is... | Then the IGES translator... |
| --- | --- |
| True | Displays the IGES-In Surfaces, Curves, and Levels dialog to the user where the user can specify levels and values. |
| false and you retrieved IImportIgesData | Does not display the IGES-In Surfaces, Curves, and Levels dialog to the user and allows you to specify the levels and values. |
| false and you did not retrieve IImportIgesData | Does not display the IGES-In Surfaces, Curves, and Levels dialog to the user and uses the default values. |

To specify levels and values when importing IGES data:

1. Set the user preference swIGESImportShowLevel to false.

2. Use [ISldWorks::GetImportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetImportFileData.html) to get IImportIgesData.

3. Use the IImportIgesData functions to specify the levels and values.

4. Use [ISldworks::LoadFile4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~LoadFile4.html) to load the file.

## Accessors

[ISldWorks::GetImportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetImportFileData.html)

## Access Diagram

[ImportIgesData](SWObjectModel.pdf#ImportIgesData)

## See Also

[IImportIgesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IImportDxfDwgData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData.html)
