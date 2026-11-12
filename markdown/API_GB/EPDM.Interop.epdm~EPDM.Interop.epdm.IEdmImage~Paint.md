---
title: "Paint Method (IEdmImage)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmImage"
member: "Paint"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage~Paint.html"
---

# Paint Method (IEdmImage)

Paints an image on the specified device context in the specified bounding rectangle.

## Syntax

### Visual Basic

```vb
Sub Paint( _
   ByVal llHDC As System.Long, _
   Optional ByRef poDestRect As EdmRect _
)
```

### C#

```csharp
void Paint(
   System.long llHDC,
   ref EdmRect poDestRect
)
```

### C++/CLI

```cpp
void Paint(
   System.int64 llHDC,
   EdmRect% poDestRect
)
```

### Parameters

- `llHDC`: Device context handle
- `poDestRect`: [EdmRect](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html) structure; contains the size and position where to draw the image; null to use the size and position of the image when it was created or the size and position that was passed in the last call to [IEdmImage::Reposition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage~Reposition.html)

## Examples

See the [IEdmImage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmImage Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage.html)
[IEdmImage Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
