---
title: "GetPreviewBitmap Method (ISwDMDocument10)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument10"
member: "GetPreviewBitmap"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html"
---

# GetPreviewBitmap Method (ISwDMDocument10)

Gets the preview bitmap (.bmp) for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewBitmap( _
   ByRef result As SwDmPreviewError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument10
Dim result As SwDmPreviewError
Dim value As System.Object

value = instance.GetPreviewBitmap(result)
```

### C#

```csharp
System.object GetPreviewBitmap(
   out SwDmPreviewError result
)
```

### C++/CLI

```cpp
System.Object^ GetPreviewBitmap(
   [Out] SwDmPreviewError result
)
```

### Parameters

- `result`: Success or error code as defined by [SwDmPreviewError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmPreviewError.html)

### Return Value

Pointer to the preview bitmap (.bmp) (an IPictureDisp*)

## VBA Syntax

See [SwDMDocument10::GetPreviewBitmap](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument10~GetPreviewBitmap.html).

## Examples

[Get Preview Bitmap of Drawing Sheet (VB.NET)](Get_Preview_Bitmap_of_Drawing_Sheet_Example_VBNET.htm)
[Get Preview Bitmap of Drawing Sheet (C#)](Get_Preview_Bitmap_of_Drawing_Sheet_Example_CSharp.htm)

## Remarks

If a drawing has multiple sheets, then a preview bitmap is created only for the drawing sheet that was active when the drawing was last saved. If you want previews for all sheets in a multiple sheet drawing, then use [ISwDMSheet2::GetPreviewPNGBitmap](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.html).

If a part or assembly has multiple configurations, then a preview bitmap is created only for the configuration that was active when the part or assembly was last saved. If you want previews for all configurations in a multiple configuration part or assembly, then use [ISwDMConfiguration7::GetPreviewPNGBitmap](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html).

This method does not work in out-of-process and some ASP.NET/IIS web applications.

## See Also

[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.html)
[ISwDMDocument10 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10_members.html)
[ISwDMDocument10::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.html)
[ISwDMDocument10::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewPNGStreamName.html)
[ISwDMDocument10::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewStreamName.html)
[ISwDMConfiguration::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetPreviewBitmap.html)
[ISwDMConfiguration::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~PreviewStreamName.html)
[ISwDMConfiguration7::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html)
[ISwDMConfiguration7::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~PreviewPNGStreamName.html)
[ISwDMConfiguration9::GetPreviewBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewBitmapBytes.html)
[ISwDMConfiguration9::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewPNGBitmapBytes.html)
[ISwDMSheet2::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.html)
[ISwDMSheet2::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmapBytes.html)
[ISwDMSheet2::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~PreviewPNGStreamName.html)
[ISwDMApplication5::GetPreviewBitmapForAnnotationFiles Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5~GetPreviewBitmapForAnnotationFiles.html)

## Availability

SOLIDWORKS Document Manager API 2008 FCS
