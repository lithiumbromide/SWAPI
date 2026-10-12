---
title: "AddMultiVariableCondition Method (IEdmSearch9)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch9"
member: "AddMultiVariableCondition"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9~AddMultiVariableCondition.html"
---

# AddMultiVariableCondition Method (IEdmSearch9)

Adds a multi-variable condition to this search.

## Syntax

### Visual Basic

```vb
Sub AddMultiVariableCondition( _
   ByVal poVariableNames() As System.String, _
   ByVal bsCondition As System.String _
)
```

### C#

```csharp
void AddMultiVariableCondition(
   System.string[] poVariableNames,
   System.string bsCondition
)
```

### C++/CLI

```cpp
void AddMultiVariableCondition(
   System.array<String^>^ poVariableNames,
   System.String^ bsCondition
)
```

### Parameters

- `poVariableNames`: Array of file or folder data card variable names (see **Remarks**)
- `bsCondition`: Condition to apply to poVariableNames (see **Remarks**)

## Examples

See the [IEdmSearch9](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html) examples.

## Remarks

Call this method before calling [IEdmSearch5::GetFirstResult](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch5~GetFirstResult.html).

Specify poVariableNames and bsCondition using the basic syntax (single-value search logic rules) as defined in [Search Syntax](SearchSyntax-epdmapi.html).

poVariableNames requires:

- \" to replace each " inside the variable name
- \\ to replace each \ inside the variable name
- " on both the left and right side of the variable name

poVariableNames supports:

- IDs in place of names
- 0 or "" to represent "any variable
- _Name to represent file/folder name

Syntactically incorrect elements in poVariableNames will generate an exception.

## See Also

[IEdmSearch9 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9.html)
[IEdmSearch9 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch9_members.html)

## Availability

SOLIDWORKS PDM Professional 2020
