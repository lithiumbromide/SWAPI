---
title: "EdmDeletedItems Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmDeletedItems"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems.html"
---

# EdmDeletedItems Structure

Contains information about deleted items.

## Syntax

### Visual Basic

```vb
Public Structure EdmDeletedItems
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmDeletedItems : System.ValueType
```

### C++/CLI

```cpp
public value class EdmDeletedItems : public System.ValueType
```

## Examples

struct EdmDeletedItems

{
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems~mlFileID.html);
integer [mlObjectType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems~mlObjectType.html);
integer [mlProjectID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems~mlProjectID.html);
string [moName](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems~moName.html);
};

## See Also

[EdmDeletedItems Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDeletedItems_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Pro 2018
