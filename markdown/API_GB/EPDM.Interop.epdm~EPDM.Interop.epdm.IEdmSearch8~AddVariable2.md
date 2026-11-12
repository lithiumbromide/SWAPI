---
title: "AddVariable2 Method (IEdmSearch8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch8"
member: "AddVariable2"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~AddVariable2.html"
---

# AddVariable2 Method (IEdmSearch8)

Adds a file or folder data card variable to this search.

## Syntax

### Visual Basic

```vb
Sub AddVariable2( _
   ByRef poIdOrName As System.Object, _
   ByRef poValue As System.Object, _
   Optional ByVal lEdmVarOp As System.Integer _
)
```

### C#

```csharp
void AddVariable2(
   ref System.object poIdOrName,
   ref System.object poValue,
   System.int lEdmVarOp
)
```

### C++/CLI

```cpp
void AddVariable2(
   System.Object^% poIdOrName,
   System.Object^% poValue,
   System.int lEdmVarOp
)
```

### Parameters

- `poIdOrName`: ID or name of variable for which to search
- `poValue`: Value or regular expression for which to search (see **Remarks**)
- `lEdmVarOp`: Operator to apply to poValue as defined in [EdmVarOp](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVarOp.html) (see **Remarks**)

## Examples

See the [IEdmSearch8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html) and [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html) examples.

## Remarks

If the search object:

- is [IEdmSearch5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5.html), then:

  - before calling this method, call [IEdmSearch8::BeginAND](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~BeginAND.html) or [IEdmSearch8::BeginOR](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8~BeginOR.html) to construct more complicated search criteria.
  - poValue may contain wildcards:

- % - any number of arbitrary characters
- _ - exactly one arbitrary character

- is created using [IEdmVault21::CreateSearch2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault21~CreateSearch2.html) (IEdmSearch9), then poValue follows basic syntax (single-value search logic rules. See [Search Syntax](SearchSyntax-epdmapi.html).) lEdmVarOp must be Nothing or null.

The number of times you could call this method was limited to 4 in SOLIDWORKS PDM Professional Version 6.0 and earlier. This restriction was removed in Version 6.1.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_EDM_KEY_NOT_FOUND: The variable name was not recognized.

## See Also

[IEdmSearch8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8.html)
[IEdmSearch8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch8_members.html)

## Availability

SOLIDWORKS PDM Professional 2018
