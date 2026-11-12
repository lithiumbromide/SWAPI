---
title: "EdmVarVal Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmVarVal"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVarVal.html"
---

# EdmVarVal Structure

Passed to [IEdmBatchItemGeneration2::AddSelection2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchItemGeneration2~AddSelection2.html) to update a variable value.

## Syntax

### Visual Basic

```vb
Public Structure EdmVarVal
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmVarVal : System.ValueType
```

### C++/CLI

```cpp
public value class EdmVarVal : public System.ValueType
```

## Examples

struct EdmVarVal{
integer [mlEdmVarValFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVarVal~mlEdmVarValFlags.html);
object [moVarIDorName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVarVal~moVarIDorName.html);
object [moValue](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVarVal~moValue.html);
};

## Examples

[Add Items (C#)](Add_Items_Example_CSharp.htm)
[Add Items (VB.NET)](Add_Items_Example_VBNET.htm)

## See Also

[EdmVarVal Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmVarVal_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[Porgramming Items](Items.htm)

## Availability

SOLIDWORKS PDM Professional 2010
