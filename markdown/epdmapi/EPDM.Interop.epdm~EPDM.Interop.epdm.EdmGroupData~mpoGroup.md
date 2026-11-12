---
title: "mpoGroup Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupData"
member: "mpoGroup"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData~mpoGroup.html"
---

# mpoGroup Field

Group interface.

## Syntax

### Visual Basic

```vb
Public mpoGroup As IEdmUserGroup5
```

### C#

```csharp
public IEdmUserGroup5 mpoGroup
```

### C++/CLI

```cpp
public:
IEdmUserGroup5^ mpoGroup
```

### Field Value

[IEdmUserGroup5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserGroup5.html)

## Remarks

This member is valid only if [EdmGroupData::mlFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData~mlFlags.html) sets the [EdmGroupDataFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupDataFlags.html).Edmgdf_GetInterface bit.

## See Also

[EdmGroupData Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData.html)
[EdmGroupData Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData_members.html)
