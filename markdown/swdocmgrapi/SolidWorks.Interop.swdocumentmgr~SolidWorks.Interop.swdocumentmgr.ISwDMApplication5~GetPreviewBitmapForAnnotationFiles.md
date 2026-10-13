---
title: "GetPreviewBitmapForAnnotationFiles Method (ISwDMApplication5)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication5"
member: "GetPreviewBitmapForAnnotationFiles"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5~GetPreviewBitmapForAnnotationFiles.html"
---

# GetPreviewBitmapForAnnotationFiles Method (ISwDMApplication5)

Gets the preview bitmap for the specified annotation file.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewBitmapForAnnotationFiles( _
   ByVal fileName As System.String, _
   ByRef result As SwDmAnnotationFileOpenError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication5
Dim fileName As System.String
Dim result As SwDmAnnotationFileOpenError
Dim value As System.Object

value = instance.GetPreviewBitmapForAnnotationFiles(fileName, result)
```

### C#

```csharp
System.object GetPreviewBitmapForAnnotationFiles(
   System.string fileName,
   out SwDmAnnotationFileOpenError result
)
```

### C++/CLI

```cpp
System.Object^ GetPreviewBitmapForAnnotationFiles(
   System.String^ fileName,
   [Out] SwDmAnnotationFileOpenError result
)
```

### Parameters

- `fileName`: Name of annotation file
- `result`: Error code as defined by [SwDmAnnotationFileOpenError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmAnnotationFileOpenError.html)

### Return Value

Pointer to the preview bitmap (.bmp) (an IPictureDisp*)

## VBA Syntax

See [SwDMApplication5::GetPreviewBitmapForAnnotationFiles](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication5~GetPreviewBitmapForAnnotationFiles.html).

## Examples

Tailor the examples for [ISwDMDocument10::GetPreviewBitmap](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html) to call this method after opening an annotation file.

## Remarks

This method is only valid for getting the preview bitmaps of the following annotation file types:

*.SLDNOTESTL

*.SLDGTOLSTL

*.SLDSFSTL

*.SLDWELDSTL

*.SLDSFFVT

*.SLDGTOLFVT

*.SLDWELDFVT

*.SLDNOTEFVT

## See Also

[ISwDMApplication5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.html)
[ISwDMApplication5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5_members.html)
[ISwDMDocument10::GetPreviewBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html)
[ISwDMDocument10::GetPreviewPNGBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.html)
[ISwDMConfiguration::GetPreviewBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetPreviewBitmap.html)
[ISwDMConfiguration7::GetPreviewPNGBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html)
[ISwDMSheet2::GetPreviewPNGBitmap Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.html)
[ISwDMSheet2::GetPreviewPNGBitmapBytes Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmapBytes.html)

## Availability

SOLIDWORKS Document Manager API 2024 SP1
