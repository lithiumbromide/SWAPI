---
title: "GetAllControls Method (IEdmCard7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCard7"
member: "GetAllControls"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard7~GetAllControls.html"
---

# GetAllControls Method (IEdmCard7)

Gets all controls in this file or folder data card.

## Syntax

### Visual Basic

```vb
Sub GetAllControls( _
   ByRef ppControlsList As System.Object() _
)
```

### C#

```csharp
void GetAllControls(
   out System.object[] ppControlsList
)
```

### C++/CLI

```cpp
void GetAllControls(
   [Out] System.array<Object^> ppControlsList
)
```

### Parameters

- `ppControlsList`: Array of [IEdmCardControl5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html)

## Examples

See the [IEdmCard7](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard7.html) example.

## See Also

[IEdmCard7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard7.html)
[IEdmCard7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard7_members.html)

## Availability

SOLIDWORKS PDM Professional 2019 SP03
