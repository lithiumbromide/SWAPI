---
title: "GetPosition Method (IEdmImage)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmImage"
member: "GetPosition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage~GetPosition.html"
---

# GetPosition Method (IEdmImage)

Gets the bounding rectangle where the image is drawn.

## Syntax

### Visual Basic

```vb
Sub GetPosition( _
   ByRef poDestRect As EdmRect _
)
```

### C#

```csharp
void GetPosition(
   out EdmRect poDestRect
)
```

### C++/CLI

```cpp
void GetPosition(
   [Out] EdmRect poDestRect
)
```

### Parameters

- `poDestRect`: [EdmRect](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html) structure; contains the size and position where to draw the image

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.

## See Also

[IEdmImage Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage.html)
[IEdmImage Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
