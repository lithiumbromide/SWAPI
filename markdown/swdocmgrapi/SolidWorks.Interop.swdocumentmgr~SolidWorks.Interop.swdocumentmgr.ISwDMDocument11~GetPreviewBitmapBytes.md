---
title: "GetPreviewBitmapBytes Method (ISwDMDocument11)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument11"
member: "GetPreviewBitmapBytes"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11~GetPreviewBitmapBytes.html"
---

# GetPreviewBitmapBytes Method (ISwDMDocument11)

Obsolete. Superseded by [ISwDMConfiguration9::GetPreviewBitmapBytes](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration9~GetPreviewBitmapBytes.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreviewBitmapBytes( _
   ByRef result As SwDmPreviewError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument11
Dim result As SwDmPreviewError
Dim value As System.Object

value = instance.GetPreviewBitmapBytes(result)
```

### C#

```csharp
System.object GetPreviewBitmapBytes(
   out SwDmPreviewError result
)
```

### C++/CLI

```cpp
System.Object^ GetPreviewBitmapBytes(
   [Out] SwDmPreviewError result
)
```

### Parameters

- `result`: Success or error code as defined by [swDmPreviewError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmPreviewError.html)

### Return Value

Preview byte array

## VBA Syntax

See [SwDMDocument11::GetPreviewBitmapBytes](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument11~GetPreviewBitmapBytes.html).

## See Also

[ISwDMDocument11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11.html)
[ISwDMDocument11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 SP5
