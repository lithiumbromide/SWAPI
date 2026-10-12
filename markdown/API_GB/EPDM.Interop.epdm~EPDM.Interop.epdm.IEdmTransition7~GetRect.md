---
title: "GetRect Method (IEdmTransition7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition7"
member: "GetRect"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7~GetRect.html"
---

# GetRect Method (IEdmTransition7)

Gets the bounding rectangle of the transition box in the workflow editor.

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

- `poRect`: [EdmRect](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html) structure; bounding rectangle

## Examples

See the [IEdmTransition7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTransition7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7.html)
[IEdmTransition7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7_members.html)
[IEdmTransition7::GetArrowVertices Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7~GetArrowVertices.html)

## Availability

SOLIDWORKS PDM Professional 2011
