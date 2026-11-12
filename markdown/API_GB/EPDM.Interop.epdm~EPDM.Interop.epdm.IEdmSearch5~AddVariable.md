---
title: "AddVariable Method (IEdmSearch5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch5"
member: "AddVariable"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~AddVariable.html"
---

# AddVariable Method (IEdmSearch5)

Obsolete. Superseded by [IEdmSearch8::AddVariable2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.html).

## Syntax

### Visual Basic

```vb
Sub AddVariable( _
   ByRef poIdOrName As System.Object, _
   ByRef poValue As System.Object _
)
```

### C#

```csharp
void AddVariable(
   ref System.object poIdOrName,
   ref System.object poValue
)
```

### C++/CLI

```cpp
void AddVariable(
   System.Object^% poIdOrName,
   System.Object^% poValue
)
```

### Parameters

- `poIdOrName`: ID or name of variable for which to search
- `poValue`: Value for which to search (see **Remarks**)

## Remarks

poValue may contain wildcards:

- % - any number of arbitrary characters
- _ - exactly one arbitrary character

The number of times you could call this method was limited to 4 in SOLIDWORKS PDM Professional Version 6.0 and earlier. This restriction was removed in Version 6.1.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_KEY_NOT_FOUND: The variable name was not recognized.

## See Also

[IEdmSearch5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html)
[IEdmSearch5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
