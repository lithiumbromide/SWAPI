---
title: "Reset Method (IEdmEnum)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnum"
member: "Reset"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~Reset.html"
---

# Reset Method (IEdmEnum)

Resets the enumerator's cursor to the position before the first element in the list.

## Syntax

### Visual Basic

```vb
Sub Reset()
```

### C#

```csharp
void Reset()
```

### C++/CLI

```cpp
void Reset();
```

## Remarks

After calling this method, you must call [IEdmEnum::MoveNext](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~MoveNext.html) before you can call [IEdmEnum::Current](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~Current.html) to get the first element in the list.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmEnum Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum.html)
[IEdmEnum Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
