---
title: "SaveBMP Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SaveBMP"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveBMP.html"
---

# SaveBMP Method (IModelDoc2)

Saves the current view as a bitmap (BMP) file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveBMP( _
   ByVal FileNameIn As System.String, _
   ByVal WidthIn As System.Integer, _
   ByVal HeightIn As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FileNameIn As System.String
Dim WidthIn As System.Integer
Dim HeightIn As System.Integer
Dim value As System.Boolean

value = instance.SaveBMP(FileNameIn, WidthIn, HeightIn)
```

### C#

```csharp
System.bool SaveBMP(
   System.string FileNameIn,
   System.int WidthIn,
   System.int HeightIn
)
```

### C++/CLI

```cpp
System.bool SaveBMP(
   System.String^ FileNameIn,
   System.int WidthIn,
   System.int HeightIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileNameIn`: Path and file name of the new BMP file
- `WidthIn`: Width of the BMP
- `HeightIn`: Height of the BMP

### Return Value

True if file is created successfully, false if not

## VBA Syntax

See [ModelDoc2::SaveBMP](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SaveBMP.html).

## Examples

[Save Model as Bitmap (C#)](Save_Model_as_Bitmap_Example_CSharp.htm)
[Save Model as Bitmap (VB.NET)](Save_Model_as_Bitmap_Example_VBNET.htm)
[Save Model as Bitmap (VBA)](Save_Model_as_Bitmap_Example_VB.htm)

## Remarks

Include the full path to the file in FilenameIn and use filename extension of .bmp.

If WidthIn or the HeightIn is less than or equal to 0, then the view size is based on the current window size.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISldWorks::GetPreviewBitmapFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmapFile.html)
[ISldWorks::GetPreviewBitmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmap.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
