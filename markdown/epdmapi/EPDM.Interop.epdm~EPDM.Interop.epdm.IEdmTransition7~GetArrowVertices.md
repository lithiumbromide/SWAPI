---
title: "GetArrowVertices Method (IEdmTransition7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmTransition7"
member: "GetArrowVertices"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7~GetArrowVertices.html"
---

# GetArrowVertices Method (IEdmTransition7)

Gets the points that make up the transition arrow in the workflow graph.

## Syntax

### Visual Basic

```vb
Sub GetArrowVertices( _
   ByRef ppoVertices() As EdmPoint _
)
```

### C#

```csharp
void GetArrowVertices(
   out EdmPoint[] ppoVertices
)
```

### C++/CLI

```cpp
void GetArrowVertices(
   [Out] array<EdmPoint>^ ppoVertices
)
```

### Parameters

- `ppoVertices`: Array of [EdmPoint](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmPoint.html) structures; one structure for each point that makes up the transition arrow

## Examples

See the [IEdmTransition7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7.html) examples.

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmTransition7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7.html)
[IEdmTransition7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7_members.html)
[IEdmTransition7::GetRect Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition7~GetRect.html)

## Availability

SOLIDWORKS PDM Professional 2011
