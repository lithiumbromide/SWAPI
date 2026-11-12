---
title: "GetValue Method (IEdmVariableValue5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableValue5"
member: "GetValue"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5~GetValue.html"
---

# GetValue Method (IEdmVariableValue5)

Gets the value of this variable in the specified configuration.

## Syntax

### Visual Basic

```vb
Function GetValue( _
   ByVal bsConfiguration As System.String _
) As System.Object
```

### C#

```csharp
System.object GetValue(
   System.string bsConfiguration
)
```

### C++/CLI

```cpp
System.Object^ GetValue(
   System.String^ bsConfiguration
)
```

### Parameters

- `bsConfiguration`: Name of configuration for which to get the value; "" for folders and file types that do not support multiple configurations

### Return Value

Value of the variable

## Examples

See the [IEdmVariableValue5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5.html) examples.

## Remarks

C++ users should use VariantInit and VariantClear to handle the VARIANT struct properly.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: No value exists for the specified configuration.

## See Also

[IEdmVariableValue5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5.html)
[IEdmVariableValue5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
