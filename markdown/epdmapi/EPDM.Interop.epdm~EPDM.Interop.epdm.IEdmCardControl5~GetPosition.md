---
title: "GetPosition Method (IEdmCardControl5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl5"
member: "GetPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~GetPosition.html"
---

# GetPosition Method (IEdmCardControl5)

Gets the dimensions and position of this control.

## Syntax

### Visual Basic

```vb
Sub GetPosition( _
   ByRef plX As System.Integer, _
   ByRef plY As System.Integer, _
   ByRef plWidth As System.Integer, _
   ByRef plHeight As System.Integer _
)
```

### C#

```csharp
void GetPosition(
   out System.int plX,
   out System.int plY,
   out System.int plWidth,
   out System.int plHeight
)
```

### C++/CLI

```cpp
void GetPosition(
   [Out] System.int plX,
   [Out] System.int plY,
   [Out] System.int plWidth,
   [Out] System.int plHeight
)
```

### Parameters

- `plX`: X-coordinate of the top-left corner of the control
- `plY`: Y-coordinate of the top-left corner of the control
- `plWidth`: Width of the control in pixels
- `plHeight`: Height of the control in pixels

## Examples

See the [IEdmCardControl6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardControl5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html)
[IEdmCardControl5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
