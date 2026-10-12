---
title: "EdmVariableData Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmVariableData"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData.html"
---

# EdmVariableData Structure

Contains information about a variable created with [IEdmVariableMgr6::AddVariables](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr6~AddVariables.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmVariableData
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmVariableData : System.ValueType
```

### C++/CLI

```cpp
public value class EdmVariableData : public System.ValueType
```

## Examples

struct EdmVariableData{
string [mbsVariableName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData~mbsVariableName.html);
EdmVariableType [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData~meType.html);
integer [mlEdmVariableFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData~mlEdmVariableFlags.html);
EdmAttributeData [mpoAttributes](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData~mpoAttributes.html);
integer [mlVariableID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData~mlVariableID.html);
};

## Examples

[Add Card Variables to Vault (VB.NET)](Add_Variables_to_Vault_Example_VBNET.htm)
[Add Card Variables to Vault (C#)](Add_Variables_to_Vault_Example_CSharp.htm)

## See Also

[EdmVariableData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
