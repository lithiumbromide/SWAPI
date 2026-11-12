---
title: "PreviewPNGStreamName Property (ISwDMConfiguration7)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration7"
member: "PreviewPNGStreamName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~PreviewPNGStreamName.html"
---

# PreviewPNGStreamName Property (ISwDMConfiguration7)

Gets the name of the stream for the PNG preview bitmap of this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PreviewPNGStreamName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration7
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

Name of the stream for the PNG preview bitmap or an empty string if preview bitmap does not exist

## VBA Syntax

See [SwDMConfiguration7::PreviewPNGStreamName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration7~PreviewPNGStreamName.html).

## Examples

[Get PNG Preview Bitmap and Stream for Configuration (C#)](Get_PNG_Preview_Bitmap_and_Stream_for_Configuration_Example_CSharp.htm)
[Get PNG Preview Bitmap and Stream for Configuration (VB.NET)](Get_PNG_Preview_Bitmap_and_Stream_for_Configuration_Example_VBNET.htm)

## See Also

[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.html)
[ISwDMConfiguration7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7_members.html)
[ISwDMConfiguration7::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html)
[ISwDMConfiguration::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetPreviewBitmap.html)
[ISwDMConfiguration::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~PreviewStreamName.html)
[ISwDMDocument10::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html)
[ISwDMDocument10::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.html)
[ISwDMDocument10::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewPNGStreamName.html)
[ISwDMDocument10::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewStreamName.html)
[ISwDMConfiguration9::GetPreviewBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewBitmapBytes.html)
[ISwDMConfiguration9::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewPNGBitmapBytes.html)

## Availability

SOLIDWORKS Document Manager API 2007 FCS
