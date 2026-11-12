---
title: "mhStatus Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmGroupData2"
member: "mhStatus"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2~mhStatus.html"
---

# mhStatus Field

Status of the group creation.

## Syntax

### Visual Basic

```vb
Public mhStatus As System.Integer
```

### C#

```csharp
public System.int mhStatus
```

### C++/CLI

```cpp
public:
System.int mhStatus
```

### Field Value

0 if successful, 1 if not

## Remarks

Call [IEdmVault5::GetErrorString](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetErrorString.html) to obtain a readable description of the error.

## See Also

[EdmGroupData2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2.html)
[EdmGroupData2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmGroupData2_members.html)
