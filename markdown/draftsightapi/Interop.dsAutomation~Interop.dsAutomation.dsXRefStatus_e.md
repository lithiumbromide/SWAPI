---
title: "dsXRefStatus_e Enumeration"
project: ""
interface: "dsXRefStatus_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsXRefStatus_e.html"
---

# dsXRefStatus_e Enumeration

Statuses returned by the GetStatus methods of external reference interfaces.

## Syntax

### Visual Basic

```vb
Public Enum dsXRefStatus_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsXRefStatus_e : System.Enum
```

### JScript

```
public enum dsXRefStatus_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsXRefStatus_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsXRefStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsXRefStatus_XrfFileNotFound | 4 |
| dsXRefStatus_XrfNotAnXref | 0 |
| dsXRefStatus_XrfResolved | 1 |
| dsXRefStatus_XrfUnloaded | 2 |
| dsXRefStatus_XrfUnreferenced | 3 |
| dsXRefStatus_XrfUnresolved | 5 |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IExternalReference::GetStatus Method ()](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetStatus.html)
[IReferenceImage::GetStatus Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetStatus.html)
[IImageDefinition::GetStatus Method ()](Interop.dsAutomation~Interop.dsAutomation.IImageDefinition~GetStatus.html)
[IPdfDefinition::GetStatus Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition~GetStatus.html)
[IPdfReference::GetStatus Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetStatus.html)
[IDgnDefinition::GetStatus Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetStatus.html)
[IDgnReference::GetStatus Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetStatus.html)
