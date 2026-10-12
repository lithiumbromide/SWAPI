---
title: "BeginAND Method (IEdmSearch8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch8"
member: "BeginAND"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~BeginAND.html"
---

# BeginAND Method (IEdmSearch8)

Begins boolean AND operation.

## Syntax

### Visual Basic

```vb
Sub BeginAND()
```

### C#

```csharp
void BeginAND()
```

### C++/CLI

```cpp
void BeginAND();
```

## Examples

See the [IEdmSearch8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html) examples.

## Remarks

After calling this method, call [IEdmSearch8::AddVariable2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.html) multiple times to further constrain the search.

Use [IEdmSearch8::EndAND](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~EndAND.html) to end the AND operation.

## See Also

[IEdmSearch8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html)
[IEdmSearch8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
