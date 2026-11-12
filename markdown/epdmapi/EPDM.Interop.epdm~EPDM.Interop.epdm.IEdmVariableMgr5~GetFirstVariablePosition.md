---
title: "GetFirstVariablePosition Method (IEdmVariableMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableMgr5"
member: "GetFirstVariablePosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~GetFirstVariablePosition.html"
---

# GetFirstVariablePosition Method (IEdmVariableMgr5)

Starts an enumeration of the variables in the vault.

## Syntax

### Visual Basic

```vb
Function GetFirstVariablePosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstVariablePosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstVariablePosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first variable in the enumeration

## Examples

[Find Data Cards with Description Variable (C#)](Find_Data_Cards_with_Description_Variable_Example_CSharp.htm)
[Find Data Cards with Description Variable (VB.NET)](Find_Data_Cards_with_Description_Variable_Example_VBNET.htm)

## Remarks

After calling this method, pass the returned position of the first variable to [IEdmVariableMgr5::GetNextVariable](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~GetNextVariable.html) to get the first variable in this list. Then call IEdmVariableMgr5::GetNextVariable repeatedly to get the rest of the variables.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmPos5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariableMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5.html)
[IEdmVariableMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
