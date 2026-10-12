---
title: "Draw Method (IEdmBitmap5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBitmap5"
member: "Draw"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5~Draw.html"
---

# Draw Method (IEdmBitmap5)

Draws this bitmap image in a window.

## Syntax

### Visual Basic

```vb
Sub Draw( _
   ByVal lWnd As System.Integer, _
   Optional ByVal lX As System.Integer, _
   Optional ByVal lY As System.Integer, _
   Optional ByVal lWidth As System.Integer, _
   Optional ByVal lHeight As System.Integer _
)
```

### C#

```csharp
void Draw(
   System.int lWnd,
   System.int lX,
   System.int lY,
   System.int lWidth,
   System.int lHeight
)
```

### C++/CLI

```cpp
void Draw(
   System.int lWnd,
   System.int lX,
   System.int lY,
   System.int lWidth,
   System.int lHeight
)
```

### Parameters

- `lWnd`: Handle of window in which to draw the bitmap image
- `lX`: X-coordinate in pixels where to position upper-left corner of image ; default is 0
- `lY`: Y-coordinate in pixels where to position upper-left corner of image; default is 0
- `lWidth`: Width in pixels of the drawn image; 0 for source image width
- `lHeight`: Height in pixels of the drawn image; 0 for source image height

## Examples

See the [IEdmBitmap5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBitmap5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5.html)
[IEdmBitmap5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBitmap5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
