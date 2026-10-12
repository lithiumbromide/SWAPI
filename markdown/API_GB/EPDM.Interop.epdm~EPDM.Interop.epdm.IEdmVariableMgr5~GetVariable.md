---
title: "GetVariable Method (IEdmVariableMgr5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVariableMgr5"
member: "GetVariable"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5~GetVariable.html"
---

# GetVariable Method (IEdmVariableMgr5)

Gets a variable with the specified ID or name.

## Syntax

### Visual Basic

```vb
Function GetVariable( _
   ByRef poIdOrName As System.Object _
) As IEdmVariable5
```

### C#

```csharp
IEdmVariable5 GetVariable(
   ref System.object poIdOrName
)
```

### C++/CLI

```cpp
IEdmVariable5^ GetVariable(
   System.Object^% poIdOrName
)
```

### Parameters

- `poIdOrName`: ID or name of variable to get

### Return Value

[IEdmVariable5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariable5.html); Null if poIdOrName is not valid

## Examples

[Batch Update Card Variables (VB.NET)](Batch_Update_Variables_Example_VBNET.htm)
[Batch Update Card Variables (C#)](Batch_Update_Variables_Example_CSharp.htm)

## Remarks

C++ users not using smart-pointer wrapper functions must release the returned pointer, IEdmVariable5.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- S_FALSE: The variable name or ID is not recognized.

## See Also

[IEdmVariableMgr5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5.html)
[IEdmVariableMgr5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2
