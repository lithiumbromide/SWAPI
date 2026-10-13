---
title: "EdmDataType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmDataType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDataType.html"
---

# EdmDataType Enumeration

Data types; used in calls to [IEdmData::Type](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData~Type.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmDataType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmDataType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmDataType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmData_File | 1 = File |
| EdmData_Folder | 2 = Folder |
| EdmData_Link | 4 = Link |
| EdmData_Nothing | 0 = No data |
| EdmData_Variable | 3 = Variable |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmData Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData.html)
[IEdmTemplate53::RunEx Method](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTemplate53~RunEx.html)
