---
title: "OpenHelp Method (IApplication)"
project: ""
interface: "IApplication"
member: "OpenHelp"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenHelp.html"
---

# OpenHelp Method (IApplication)

Opens the specified system help topic in the specified system help.

## Syntax

### Visual Basic

```vb
Function OpenHelp( _
   ByVal HelpID As System.Integer, _
   ByVal ProductID As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool OpenHelp(
   System.int HelpID,
   System.int ProductID
)
```

### JScript

```
function OpenHelp(
   HelpID : System.int,
   ProductID : System.int
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool OpenHelp(
   System.int HelpID,
   System.int ProductID
)
```

### C++/CLI

```cpp
System.bool OpenHelp(
   System.int HelpID,
   System.int ProductID
)
```

### Parameters

- `HelpID`: ID of the system help topic to open
- `ProductID`: Product ID of the system help

### Return Value

True if the system help topic successfully opened, false if not

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight 2019 SP0
