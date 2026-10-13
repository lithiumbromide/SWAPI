---
title: "MinimumSupportedClientSP Property (IEdmVault18)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmVault18"
member: "MinimumSupportedClientSP"
kind: "property"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault18~MinimumSupportedClientSP.html"
---

# MinimumSupportedClientSP Property (IEdmVault18)

Gets the minimum client service pack supported by this vault's views.

## Syntax

### Visual Basic

```vb
ReadOnly Property MinimumSupportedClientSP As System.Integer
```

### C#

```csharp
System.int MinimumSupportedClientSP {get;}
```

### C++/CLI

```cpp
property System.int MinimumSupportedClientSP {
   System.int get();
}
```

### Property Value

Minimum supported client service pack (e.g., 0, 1, 2, 3, 4, 5)

## Remarks

As of SOLIDWORKS PDM Professional 2017 SP01, client/server minor version mismatches are supported. For example, if this method returns "0", then for the current major version (e.g., 2017), an SP0 client machine works with vault views created with other service packs.

## See Also

[IEdmVault18 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault18.html)
[IEdmVault18 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault18_members.html)

## Availability

SOLIDWORKS PDM Professional 2017 SP01
