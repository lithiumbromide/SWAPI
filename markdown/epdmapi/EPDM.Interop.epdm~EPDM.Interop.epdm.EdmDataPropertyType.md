---
title: "EdmDataPropertyType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmDataPropertyType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmDataPropertyType.html"
---

# EdmDataPropertyType Enumeration

Property types; used in calls to [IEdmData::Get](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData~Get.html) and [IEdmData::Set](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmData~Set.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmDataPropertyType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmDataPropertyType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmDataPropertyType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmProp_ID | 1 = Database ID |
| EdmProp_LinkPath | 8 = Path to linked file |
| EdmProp_Name | 4 = Name of a file, folder, variable, etc. |
| EdmProp_Nothing | 0 = Invalid property |
| EdmProp_Object | 3 = IEdmObject5 |
| EdmProp_ObjectType | 2 = EdmObjectType |
| EdmProp_Path | 5 = File or folder path |
| EdmProp_Value | 6 = Variable value |
| EdmProp_Vault | 7 = IEdmVault5 |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
