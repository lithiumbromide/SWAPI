---
title: "OpenChmHelp Method (IApplication)"
project: ""
interface: "IApplication"
member: "OpenChmHelp"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenChmHelp.html"
---

# OpenChmHelp Method (IApplication)

Opens the specified help topic in the specified CHM file.

## Syntax

### Visual Basic

```vb
Function OpenChmHelp( _
   ByVal HelpID As System.Integer, _
   ByVal ChmFile As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool OpenChmHelp(
   System.int HelpID,
   System.string ChmFile
)
```

### JScript

```
function OpenChmHelp(
   HelpID : System.int,
   ChmFile : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool OpenChmHelp(
   System.int HelpID,
   System.string* ChmFile
)
```

### C++/CLI

```cpp
System.bool OpenChmHelp(
   System.int HelpID,
   System.String^ ChmFile
)
```

### Parameters

- `HelpID`: ID of help topic to open
- `ChmFile`: Full pathname of the help CHM

### Return Value

True if the help topic successfully opened, false if not

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::OpenWebHelp Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenWebHelp.html)

## Availability

DraftSight 2019 SP0
