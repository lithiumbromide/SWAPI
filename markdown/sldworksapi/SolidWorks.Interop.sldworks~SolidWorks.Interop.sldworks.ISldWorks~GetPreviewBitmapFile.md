---
title: "GetPreviewBitmapFile Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetPreviewBitmapFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmapFile.html"
---

# GetPreviewBitmapFile Method (ISldWorks)

Gets the specified preview bitmap of a document and saves it as a Windows bitmap file (.bmp) using the specified filename.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewBitmapFile( _
   ByVal DocumentPath As System.String, _
   ByVal ConfigName As System.String, _
   ByVal BitMapFile As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocumentPath As System.String
Dim ConfigName As System.String
Dim BitMapFile As System.String
Dim value As System.Boolean

value = instance.GetPreviewBitmapFile(DocumentPath, ConfigName, BitMapFile)
```

### C#

```csharp
System.bool GetPreviewBitmapFile(
   System.string DocumentPath,
   System.string ConfigName,
   System.string BitMapFile
)
```

### C++/CLI

```cpp
System.bool GetPreviewBitmapFile(
   System.String^ DocumentPath,
   System.String^ ConfigName,
   System.String^ BitMapFile
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocumentPath`: Path and file name of the SOLIDWORKS document whose preview bitmap (.bmp) you want to save
- `ConfigName`: Name of the configuration
- `BitMapFile`: Filename for the preview

### Return Value

True if the preview bitmap (.bmp) is saved, false if not

## VBA Syntax

See [SldWorks::GetPreviewBitmapFile](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetPreviewBitmapFile.html).

## Examples

[Save Configuration Data (C#)](Save_Configuration_Data_Example_CSharp.htm)
[Save Configuration Data (VB.NET)](Save_Configuration_Data_Example_VBNET.htm)
[Save Configuration Data (VBA)](Save_Configuration_Data_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetPreviewBitmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmap.html)
[ISldWorks::PreviewDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDoc.html)
[ISldWorks::PreviewDocx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDocx64.html)
[IModelDoc2::SaveBMP Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveBMP.html)

## Availability

SOLIDWORKS 2008 Sp2, Revision Number 16.2
