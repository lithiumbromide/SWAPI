---
title: "GetUpdatedPaths Method (IEdmRefItem2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmRefItem2"
member: "GetUpdatedPaths"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem2~GetUpdatedPaths.html"
---

# GetUpdatedPaths Method (IEdmRefItem2)

Gets the old and new paths of references that have been moved or renamed by another client.

## Syntax

### Visual Basic

```vb
Sub GetUpdatedPaths( _
   ByRef ppoUpdatedPathArr() As EdmUpdatedRefPath _
)
```

### C#

```csharp
void GetUpdatedPaths(
   out EdmUpdatedRefPath[] ppoUpdatedPathArr
)
```

### C++/CLI

```cpp
void GetUpdatedPaths(
   [Out] array<EdmUpdatedRefPath>^ ppoUpdatedPathArr
)
```

### Parameters

- `ppoUpdatedPathArr`: Array of [EdmUpdatedRefPath](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUpdatedRefPath.html)s

## See Also

[IEdmRefItem2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem2.html)
[IEdmRefItem2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmRefItem2_members.html)

## Availability

SOLIDWORKS PDM Professional 2021 SP04
