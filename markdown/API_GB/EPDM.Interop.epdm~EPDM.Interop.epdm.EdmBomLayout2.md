---
title: "EdmBomLayout2 Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmBomLayout2"
member: ""
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout2.html"
---

# EdmBomLayout2 Structure

Contains information about a Bill of Materials layout.

## Syntax

### Visual Basic

```vb
Public Structure EdmBomLayout2
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmBomLayout2 : System.ValueType
```

### C++/CLI

```cpp
public value class EdmBomLayout2 : public System.ValueType
```

## Examples

struct EdmBomLayout2{
integer [mlLayoutID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout~mlLayoutID.html);
[EdmBomType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout2~meType.html);
string [mbsLayoutName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout~mbsLayoutName.html);
};

## Remarks

This structure:

- Extends [EdmBomLayout](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout.html).
- Is used in [IEdmBomMgr2::GetBomLayouts2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2~GetBomLayouts2.html) to get all BOM layouts and BOM types.

## See Also

[EdmBomLayout2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmBomLayout2_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2020
