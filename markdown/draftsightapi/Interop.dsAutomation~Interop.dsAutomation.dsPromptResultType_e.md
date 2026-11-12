---
title: "dsPromptResultType_e Enumeration"
project: ""
interface: "dsPromptResultType_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsPromptResultType_e.html"
---

# dsPromptResultType_e Enumeration

Types of inputs performed for [ICommandMessage](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html) methods that prompt for input.

## Syntax

### Visual Basic

```vb
Public Enum dsPromptResultType_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsPromptResultType_e : System.Enum
```

### JScript

```
public enum dsPromptResultType_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsPromptResultType_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsPromptResultType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsPromptResultType_Cancel | 3 = Input was canceled |
| dsPromptResultType_Failed | 0 = Error occurred |
| dsPromptResultType_Keyword | 2 = Input was a keyword |
| dsPromptResultType_None | 4 = No input was performed |
| dsPromptResultType_Value | 1 = Input was a value |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
