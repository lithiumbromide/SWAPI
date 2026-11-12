---
title: "mpoGroup Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupData2"
member: "mpoGroup"
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mpoGroup.html"
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

This member is valid only if [EdmGroupData2::mlFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mlFlags.html) sets the [EdmGroupDataFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupDataFlags.html).Edmgdf_GetInterface bit and [EdmGroupData2::mhStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mhStatus.html) is S_OK (0).

## See Also

[EdmGroupData2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2.html)
[EdmGroupData2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2_members.html)
