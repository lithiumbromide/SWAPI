---
title: "GetNextVariable Method (IEdmVariableMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableMgr5"
member: "GetNextVariable"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~GetNextVariable.html"
---

# GetNextVariable Method (IEdmVariableMgr5)

Gets the next variable in an enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextVariable( _
   ByVal poPos As IEdmPos5 _
) As IEdmVariable5
```

### C#

```csharp
IEdmVariable5 GetNextVariable(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmVariable5^ GetNextVariable(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next variable in the list

### Return Value

[IEdmVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5.html)

## Examples

[Find Data Cards with Description Variable (C#)](Find_Data_Cards_with_Description_Variable_Example_CSharp.htm)
[Find Data Cards with Description Variable (VB.NET)](Find_Data_Cards_with_Description_Variable_Example_VBNET.htm)

## Remarks

Before calling this method the first time, you must populate poPos with the interface to the position of the first variable in the list, IEdmPos5. Call [IEdmVariableMgr5::GetFirstVariablePosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~GetFirstVariablePosition.html) to obtain poPos.

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the variables in the list.

Be sure to call [IEdmPos5::IsNull](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5~IsNull.html) before you call this method to ensure you have not reached the end of the enumeration.

C++ users not using smart-pointer wrapper functions must release the returned interface, IEdmVariable5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmVariableMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5.html)
[IEdmVariableMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
