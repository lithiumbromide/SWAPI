---
title: "GetFirstAttributePosition Method (IEdmVariableValue5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableValue5"
member: "GetFirstAttributePosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5~GetFirstAttributePosition.html"
---

# GetFirstAttributePosition Method (IEdmVariableValue5)

Starts an enumeration of the attributes mapped to this variable.

## Syntax

### Visual Basic

```vb
Function GetFirstAttributePosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstAttributePosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstAttributePosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first attribute in the enumeration

## Remarks

After calling this method, pass the returned position of the first attribute to [IEdmVariableValue5::GetNextAttribute](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5~GetNextAttribute.html) to get the first attribute in this list. Then call IEdmVariableValue5::GetNextAttribute repeatedly to get the rest of the variables.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariableValue5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5.html)
[IEdmVariableValue5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableValue5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
