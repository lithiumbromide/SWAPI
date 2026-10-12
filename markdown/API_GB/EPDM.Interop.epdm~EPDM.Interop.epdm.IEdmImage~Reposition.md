---
title: "Reposition Method (IEdmImage)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmImage"
member: "Reposition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage~Reposition.html"
---

# Reposition Method (IEdmImage)

Changes the bounding rectangle where to draw the image.

## Syntax

### Visual Basic

```vb
Sub Reposition( _
   ByRef poDestRect As EdmRect, _
   Optional ByVal eRefresh As EdmRepaintType _
)
```

### C#

```csharp
void Reposition(
   ref EdmRect poDestRect,
   EdmRepaintType eRefresh
)
```

### C++/CLI

```cpp
void Reposition(
   EdmRect% poDestRect,
   EdmRepaintType eRefresh
)
```

### Parameters

- `poDestRect`: [EdmRect](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html) structure; size and position where to draw the image
- `eRefresh`: Type of refresh of the window as defined in [EdmRepaintType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRepaintType.html)

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmImage Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage.html)
[IEdmImage Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
