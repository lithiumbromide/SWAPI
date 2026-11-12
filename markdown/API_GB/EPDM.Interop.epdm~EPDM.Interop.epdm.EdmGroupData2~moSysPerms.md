---
title: "moSysPerms Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupData2"
member: "moSysPerms"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~moSysPerms.html"
---

# moSysPerms Field

Group system permissions.

## Syntax

### Visual Basic

```vb
Public moSysPerms As EdmSysPerm()
```

### C#

```csharp
public EdmSysPerm[] moSysPerms
```

### C++/CLI

```cpp
public:
array<EdmSysPerm>^ moSysPerms
```

### Field Value

Array of [EdmSysPerm](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysPerm.html) numbers

## Remarks

EdmSysPerm numbers replace the older [EdmSysRightFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmSysRightFlags.html) bits that were used in [EdmGroupData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData.html).

## See Also

[EdmGroupData2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2.html)
[EdmGroupData2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2_members.html)
