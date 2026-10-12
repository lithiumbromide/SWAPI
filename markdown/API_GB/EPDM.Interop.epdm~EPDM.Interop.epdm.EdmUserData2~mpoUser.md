---
title: "mpoUser Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserData2"
member: "mpoUser"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2~mpoUser.html"
---

# mpoUser Field

User's interface if [mlFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2~mlFlags.html) contains the [edmUserDataFlags.edmudf_GetInterface](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataFlags.html) and [mhStatus](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2~mhStatus.html) is S_OK (0), otherwise the pointer is null.

## Syntax

### Visual Basic

```vb
Public mpoUser As IEdmUser6
```

### C#

```csharp
public IEdmUser6 mpoUser
```

### C++/CLI

```cpp
public:
IEdmUser6^ mpoUser
```

## Examples

See the [EdmUserData2](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html) examples.

## See Also

[EdmUserData2 Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2.html)
[EdmUserData2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserData2_members.html)
