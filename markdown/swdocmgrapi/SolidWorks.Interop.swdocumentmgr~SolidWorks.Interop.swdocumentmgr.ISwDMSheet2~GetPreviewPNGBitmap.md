---
title: "GetPreviewPNGBitmap Method (ISwDMSheet2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet2"
member: "GetPreviewPNGBitmap"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.html"
---

# GetPreviewPNGBitmap Method (ISwDMSheet2)

Gets the PNG preview bitmap (.png) for this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewPNGBitmap( _
   ByRef result As SwDmPreviewError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet2
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

Pointer to the preview bitmap (.png) (an IPictureDisp*)

## VBA Syntax

See [SwDMSheet2::GetPreviewPNGBitmap](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet2~GetPreviewPNGBitmap.html).

## Examples

[Get Preview Bitmaps of Drawing Sheets (C#)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_CSharp.htm)
[Get Preview Bitmaps of Drawing Sheets (VB.NET)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_VBNET.htm)

## Remarks

This method does not work in out-of-process and in ASP.NET/IIS web applications.

## See Also

[ISwDMSheet2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2.html)
[ISwDMSheet2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2_members.html)
[ISwDMSheet2::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmapBytes.html)
[ISwDMSheet2::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~PreviewPNGStreamName.html)
[ISwDMConfiguration7::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html)
[ISwDMConfiguration9::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewPNGBitmapBytes.html)
[ISwDMConfiguration7::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~PreviewPNGStreamName.html)
[ISwDMDocument10::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.html)
[ISwDMDocument10::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewPNGStreamName.html)
[ISwDMDocument10::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html)
[ISwDMDocument10::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewStreamName.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP3
