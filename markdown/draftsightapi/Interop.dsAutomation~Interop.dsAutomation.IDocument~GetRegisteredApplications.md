---
title: "GetRegisteredApplications Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetRegisteredApplications"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html"
---

# GetRegisteredApplications Method (IDocument)

Gets the names of the registered applications for the document's [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html).

## Syntax

### Visual Basic

```vb
Function GetRegisteredApplications() As System.Object
```

### C#

```csharp
System.object GetRegisteredApplications()
```

### JScript

```
function GetRegisteredApplications() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetRegisteredApplications();
```

### C++/CLI

```cpp
System.Object^ GetRegisteredApplications();
```

### Return Value

Array of the names of the registered applications for the document's custom data (see **Remarks**)

## Remarks

The name of a registered application should be unique so that its custom data is not confused with that of other programs. A registered application name can contain letters, numbers, and these special characters: $ (dollar sign), - (hyphen), and _ (underscore).

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)

## Availability

DraftSight V1R1.2
