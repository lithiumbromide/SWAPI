---
title: "GetPreviewPNGBitmap Method (ISwDMConfiguration7)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration7"
member: "GetPreviewPNGBitmap"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html"
---

# GetPreviewPNGBitmap Method (ISwDMConfiguration7)

Gets the PNG preview bitmap for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewPNGBitmap( _
   ByRef result As SwDmPreviewError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration7
Dim result As SwDmPreviewError
Dim value As System.Object

value = instance.GetPreviewPNGBitmap(result)
```

### C#

```csharp
System.object GetPreviewPNGBitmap(
   out SwDmPreviewError result
)
```

### C++/CLI

```cpp
System.Object^ GetPreviewPNGBitmap(
   [Out] SwDmPreviewError result
)
```

### Parameters

- `result`: Success or error code as defined by [swDmPreviewError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmPreviewError.html)

### Return Value

Pointer to the PNG preview bitmap (an IPictureDisp*)

## VBA Syntax

See [SwDMConfiguration7::GetPreviewPNGBitmap](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration7~GetPreviewPNGBitmap.html).

## Examples

[Get PNG Preview Bitmap and Stream for Configuration (C#)](Get_PNG_Preview_Bitmap_and_Stream_for_Configuration_Example_CSharp.htm)
[Get PNG Preview Bitmap and Stream for Configuration (VB.NET)](Get_PNG_Preview_Bitmap_and_Stream_for_Configuration_Example_VBNET.htm)

## Remarks

This method does not work in out-of-process and some ASP.NET/IIS web applications.

## See Also

[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.html)
[ISwDMConfiguration7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7_members.html)
[ISwDMConfiguration::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetPreviewBitmap.html)
[ISwDMConfiguration::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~PreviewStreamName.html)
[ISwDMConfiguration7::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~PreviewPNGStreamName.html)
[ISwDocument10::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html)
[ISwDocument10::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.html)
[ISwDocument10::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewPNGStreamName.html)
[ISwDocument10::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewStreamName.html)
[ISwDocument11::GetPreviewBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11~GetPreviewBitmapBytes.html)
[ISwDocument11::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11~GetPreviewPNGBitmapBytes.html)
[ISwSheet2::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.html)
[ISwSheet2::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmapBytes.html)
[ISwSheet2::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~PreviewPNGStreamName.html)

## Availability

SOLIDWORKS Document Manager API 2007 FCS
