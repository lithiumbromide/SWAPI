---
title: "EdmAttributeData Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAttributeData"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAttributeData.html"
---

# EdmAttributeData Structure

Contains information about an attribute mapping in a variable ([EdmVariableData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVariableData.html)).

## Syntax

### Visual Basic

```vb
Public Structure EdmAttributeData
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmAttributeData : System.ValueType
```

### C++/CLI

```cpp
public value class EdmAttributeData : public System.ValueType
```

## Examples

struct EdmAttributeData{
string [mbsAttribName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAttributeData~mbsAttribName.html);
string [mbsBlockName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAttributeData~mbsBlockName.html);
string [mbsExtensions](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAttributeData~mbsExtensions.html);
};

## Examples

[Add Card Variables to Vault (VB.NET)](Add_Variables_to_Vault_Example_VBNET.htm)
[Add Card Variables to Vault (C#)](Add_Variables_to_Vault_Example_CSharp.htm)

## Remarks

Used by [IEdmVariableMgr6::AddVariables](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVariableMgr6~AddVariables.html) to create new variables.

## See Also

[EdmAttributeData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAttributeData_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2007
