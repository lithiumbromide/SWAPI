---
title: "GetValidation Method (IEdmCardControl5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCardControl5"
member: "GetValidation"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~GetValidation.html"
---

# GetValidation Method (IEdmCardControl5)

Gets the input validation criteria for this control.

## Syntax

### Visual Basic

```vb
Function GetValidation( _
   ByRef poMin As System.Object, _
   ByRef poMax As System.Object _
) As EdmVariableType
```

### C#

```csharp
EdmVariableType GetValidation(
   out System.object poMin,
   out System.object poMax
)
```

### C++/CLI

```cpp
EdmVariableType GetValidation(
   [Out] System.Object^ poMin,
   [Out] System.Object^ poMax
)
```

### Parameters

- `poMin`: Minimum limit; minimum number of characters in a control of type, EdmVariableType.EdmVarType_Text
- `poMax`: Maximum limit for this control's value; maximum number of characters in a control of type, EdmVariableType.EdmVarType_Text

### Return Value

Data type to validate as defined in [EdmVariableType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableType.html)

## Examples

See the [IEdmCardControl6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl6.html) examples.

## Remarks

If a card control has input validation, the user is unable to click **OK** or **Apply** until all validation conditions are met.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCardControl5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5.html)
[IEdmCardControl5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
