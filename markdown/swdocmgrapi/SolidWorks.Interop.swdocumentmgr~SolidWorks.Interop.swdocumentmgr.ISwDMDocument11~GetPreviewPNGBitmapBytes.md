---
title: "GetPreviewPNGBitmapBytes Method (ISwDMDocument11)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument11"
member: "GetPreviewPNGBitmapBytes"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11~GetPreviewPNGBitmapBytes.html"
---

# GetPreviewPNGBitmapBytes Method (ISwDMDocument11)

Obsolete. Superseded by [ISwDMConfiguration9::GetPreviewPNGBitmapBytes](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewPNGBitmapBytes.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewPNGBitmapBytes( _
   ByRef result As SwDmPreviewError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument11
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

See [SwDMDocument11::GetPreviewPNGBitmapBytes](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument11~GetPreviewPNGBitmapBytes.html).

## Examples

## See Also

[ISwDMDocument11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11.html)
[ISwDMDocument11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 SP5
