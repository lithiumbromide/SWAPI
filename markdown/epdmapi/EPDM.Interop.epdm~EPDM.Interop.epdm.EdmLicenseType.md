---
title: "EdmLicenseType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmLicenseType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicenseType.html"
---

# EdmLicenseType Enumeration

Types of license types, which are used in struct [EdmLicense](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLicense.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmLicenseType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmLicenseType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmLicenseType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmLic_Contributor | 2 = Contributor and web client license |
| EdmLic_Editor | 1 = Editor license |
| EdmLic_Processor | 4 = Processor license |
| EdmLic_Viewer | 3 = Viewer (read-only) license |

## Remarks

See the SOLIDWORKS PDM Professional client Help file for more information about what you can or cannot do with respective license type.

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
