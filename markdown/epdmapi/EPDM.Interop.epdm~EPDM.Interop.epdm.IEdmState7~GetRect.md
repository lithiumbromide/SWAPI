---
title: "GetRect Method (IEdmState7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState7"
member: "GetRect"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState7~GetRect.html"
---

# GetRect Method (IEdmState7)

Gets the bounding rectangle of the state box displayed in the workflow editor.

## Syntax

### Visual Basic

```vb
Sub GetRect( _
   ByRef poRect As EdmRect _
)
```

### C#

```csharp
void GetRect(
   out EdmRect poRect
)
```

### C++/CLI

```cpp
void GetRect(
   [Out] EdmRect poRect
)
```

### Parameters

- `poRect`: [EdmRect](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html) structure; bounding rectangle of the state box displayed in the workflow editor

## Examples

See the [IEdmState7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState7.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmState7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState7.html)
[IEdmState7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState7_members.html)
[IEdmTransition7::GetRect Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7~GetRect.html)
[IEdmTransition7::GetArrowVertices Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7~GetArrowVertices.html)

## Availability

SOLIDWORKS PDM Professional 2011
