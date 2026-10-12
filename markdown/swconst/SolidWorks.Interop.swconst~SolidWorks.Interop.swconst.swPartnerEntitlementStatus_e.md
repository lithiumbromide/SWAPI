---
title: "swPartnerEntitlementStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPartnerEntitlementStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartnerEntitlementStatus_e.html"
---

# swPartnerEntitlementStatus_e Enumeration

Partner entitlement status.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPartnerEntitlementStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPartnerEntitlementStatus_e
```

### C#

```csharp
public enum swPartnerEntitlementStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPartnerEntitlementStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPEAddinGUIDMismatch | 4 or 0x4 |
| swPEAddinNameMismatch | 2 or 0x2 |
| swPEFail | 1 or 0x1 |
| swPELicenseError | 64 or 0x40 |
| swPELicenseExpired | 16 or 0x10 |
| swPESuccess | 0 or 0x0 |
| swPETierMismatch | 32 or 0x20 |
| swPEVersionMismatch | 8 or 0x8 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
