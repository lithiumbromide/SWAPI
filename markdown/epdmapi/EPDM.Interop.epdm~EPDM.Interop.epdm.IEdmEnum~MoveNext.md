---
title: "MoveNext Method (IEdmEnum)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmEnum"
member: "MoveNext"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~MoveNext.html"
---

# MoveNext Method (IEdmEnum)

Forwards the enumeration cursor to the next element in the list.

## Syntax

### Visual Basic

```vb
Function MoveNext() As System.Boolean
```

### C#

```csharp
System.bool MoveNext()
```

### C++/CLI

```cpp
System.bool MoveNext();
```

### Return Value

True if the cursor moved to the next element successfully, false if not

## Remarks

This method is used implicitly in the For Each command loops of .NET programs.

After calling this method, call [IEdmEnum::Current](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum~Current.html) to access the element currently pointed to by the enumerator's cursor.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmEnum Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum.html)
[IEdmEnum Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
