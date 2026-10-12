---
title: "PreviewPNGStreamName Property (ISwDMSheet2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet2"
member: "PreviewPNGStreamName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~PreviewPNGStreamName.html"
---

# PreviewPNGStreamName Property (ISwDMSheet2)

Gets the name of the stream for the preview bitmap (.png) of this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PreviewPNGStreamName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet2
Dim value As System.String

value = instance.PreviewPNGStreamName
```

### C#

```csharp
System.string PreviewPNGStreamName {get;}
```

### C++/CLI

```cpp
property System.String^ PreviewPNGStreamName {
   System.String^ get();
}
```

### Property Value

Name of the stream for the preview bitmap (.png) or an empty string if preview bitmap (.png) does not exist

## VBA Syntax

See [SwDMSheet2::PreviewPNGStreamName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet2~PreviewPNGStreamName.html).

## Examples

[Get Preview Bitmaps of Drawing Sheet (C#)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_CSharp.htm)
[Get Preview Bitmaps of Drawing Sheet (VB.NET)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_VBNET.htm)

## See Also

[ISwDMSheet2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2.html)
[ISwDMSheet2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2_members.html)
[ISwDMSheet2::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.html)
[ISwDMSheet2::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmapBytes.html)
[ISwDMDocument10::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.html)
[ISwDMDocument10::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewPNGStreamName.html)
[ISwDMConfiguration9::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewPNGBitmapBytes.html)
[ISwDMConfiguration7::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html)
[ISwDMConfiguration7::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~PreviewPNGStreamName.html)
[ISwDMDoucment10::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html)
[ISwDMDocument10::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewStreamName.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP3
