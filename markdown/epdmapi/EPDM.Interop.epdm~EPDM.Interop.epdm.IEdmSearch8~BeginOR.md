---
title: "BeginOR Method (IEdmSearch8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch8"
member: "BeginOR"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~BeginOR.html"
---

# BeginOR Method (IEdmSearch8)

Begins boolean OR operation.

## Syntax

### Visual Basic

```vb
Sub BeginOR()
```

### C#

```csharp
void BeginOR()
```

### C++/CLI

```cpp
void BeginOR();
```

## Remarks

After calling this method, call [IEdmSearch8::AddVariable2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.html) multiple times to further constrain the search.

Use [IEdmSearch8::EndOR](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~EndAND.html) to end the OR operation.

## See Also

[IEdmSearch8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html)
[IEdmSearch8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
