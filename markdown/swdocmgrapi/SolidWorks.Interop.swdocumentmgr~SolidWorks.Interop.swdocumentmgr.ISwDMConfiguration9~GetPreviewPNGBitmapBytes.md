---
title: "GetPreviewPNGBitmapBytes Method (ISwDMConfiguration9)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration9"
member: "GetPreviewPNGBitmapBytes"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewPNGBitmapBytes.html"
---

# GetPreviewPNGBitmapBytes Method (ISwDMConfiguration9)

Gets the preview PNG byte array for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewPNGBitmapBytes( _
   ByRef result As SwDmPreviewError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration9
Dim result As SwDmPreviewError
Dim value As System.Object

value = instance.GetPreviewPNGBitmapBytes(result)
```

### C#

```csharp
System.object GetPreviewPNGBitmapBytes(
   out SwDmPreviewError result
)
```

### C++/CLI

```cpp
System.Object^ GetPreviewPNGBitmapBytes(
   [Out] SwDmPreviewError result
)
```

### Parameters

- `result`: Success or error code as defined by [swDmPreviewError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmPreviewError.html)

### Return Value

Preview PNG byte array

## VBA Syntax

See [SwDMConfiguration9::GetPreviewPNGBitmapBytes](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration9~GetPreviewPNGBitmapBytes.html).

## See Also

[ISwDMConfiguration9 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9.html)
[ISwDMConfiguration9 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9_members.html)
[ISwDMConfiguration9::GetPreviewBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewBitmapBytes.html)
[ISwDMConfiguration::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetPreviewBitmap.html)
[ISwDMConfiguration::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~PreviewStreamName.html)
[ISwDMConfiguration7::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~GetPreviewPNGBitmap.html)
[ISwDMConfiguration7::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~PreviewPNGStreamName.html)
[ISwDMDocument10::GetPreviewBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewBitmap.html)
[ISwDMDocument10::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetPreviewPNGBitmap.html)
[ISwDMDocument10::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewPNGStreamName.html)
[ISwDMDocument10::PreviewStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~PreviewStreamName.html)
[ISwDMSheet2::GetPreviewPNGBitmap Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmap.html)
[ISwDMSheet2::GetPreviewPNGBitmapBytes Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~GetPreviewPNGBitmapBytes.html)
[ISwDMSheet2::PreviewPNGStreamName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2~PreviewPNGStreamName.html)

## Availability

SOLIDWORKS Document Manager API 2008 SP4
