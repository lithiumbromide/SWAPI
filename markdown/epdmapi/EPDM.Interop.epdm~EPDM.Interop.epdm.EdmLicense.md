---
title: "EdmLicense Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmLicense"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicense.html"
---

# EdmLicense Structure

Contains information about a license type and is returned by [IEdmVault11::GetLicense](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault11~GetLicense.html).

## Syntax

### Visual Basic

```vb
Public Structure EdmLicense
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmLicense : System.ValueType
```

### C++/CLI

```cpp
public value class EdmLicense : public System.ValueType
```

## Examples

struct EdmLicense

{
[enum EdmLicenseType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicenseType.html) [meType](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicense~meType.html);
integer [mlUserCount](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicense~mlUserCount.html);
};

## Examples

[Vault Utilities (VB.NET)](Vault_Utilities_Example_VBNET.htm)
[Vault Utilities (C#)](Vault_Utilities_Example_CSharp.htm)

## See Also

[EdmLicense Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicense_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2010
