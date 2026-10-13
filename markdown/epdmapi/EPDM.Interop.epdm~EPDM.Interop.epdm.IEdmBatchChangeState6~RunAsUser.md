---
title: "RunAsUser Method (IEdmBatchChangeState6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchChangeState6"
member: "RunAsUser"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState6~RunAsUser.html"
---

# RunAsUser Method (IEdmBatchChangeState6)

Transitions files with another user's credentials.

## Syntax

### Visual Basic

```vb
Sub RunAsUser( _
   ByVal lParentWnd As System.Integer, _
   ByVal bsRunASUserName As System.String, _
   ByVal bsRunAsPassword As System.String _
)
```

### C#

```csharp
void RunAsUser(
   System.int lParentWnd,
   System.string bsRunASUserName,
   System.string bsRunAsPassword
)
```

### C++/CLI

```cpp
void RunAsUser(
   System.int lParentWnd,
   System.String^ bsRunASUserName,
   System.String^ bsRunAsPassword
)
```

### Parameters

- `lParentWnd`: Parent window handle that is passed to add-ins that are notified about file state changes in the vault
- `bsRunASUserName`: User name to use to transition the files
- `bsRunAsPassword`: Password for bsRunASUserName

## Examples

See the [IEdmBatchChangeState6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState6.html) examples.

## See Also

[IEdmBatchChangeState6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState6.html)
[IEdmBatchChangeState6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchChangeState6_members.html)

## Availability

SOLIDWORKS PDM Professional 2024
