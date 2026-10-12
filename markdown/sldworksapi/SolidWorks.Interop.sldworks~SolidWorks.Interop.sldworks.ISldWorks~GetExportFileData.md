---
title: "GetExportFileData Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetExportFileData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetExportFileData.html"
---

# GetExportFileData Method (ISldWorks)

Gets the data interface for the specified file type to which to export one or more drawing sheets.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExportFileData( _
   ByVal FileType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileType As System.Integer
Dim value As System.Object

value = instance.GetExportFileData(FileType)
```

### C#

```csharp
System.object GetExportFileData(
   System.int FileType
)
```

### C++/CLI

```cpp
System.Object^ GetExportFileData(
   System.int FileType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileType`: File type as defined in [swExportDataFileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportDataFileType_e.html)

### Return Value

[Data interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExportPdfData.html) for the specified file type to which to export one or more drawing sheets

## VBA Syntax

See [SldWorks::GetExportFileData](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetExportFileData.html).

## Examples

[Save File As PDF (VBA)](Save_File_as_PDF_Example_VB.htm)
[Save File as PDF (C#)](Save_File_as_PDF_Example_CSharp.htm)
[Save File as PDF (VB.NET)](Save_File_as_PDF_Example_VBNET.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15.1
