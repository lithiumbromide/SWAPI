---
title: "RemoveUserInterface Method (IApplication)"
project: ""
interface: "IApplication"
member: "RemoveUserInterface"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~RemoveUserInterface.html"
---

# RemoveUserInterface Method (IApplication)

Removes an add-in's user interface from the DraftSight user interface.

## Syntax

### Visual Basic

```vb
Sub RemoveUserInterface( _
   ByVal ApiUuid As System.String _
)
```

### C#

```csharp
void RemoveUserInterface(
   System.string ApiUuid
)
```

### JScript

```
function RemoveUserInterface(
   ApiUuid : System.String
);
```

### Managed Extensions for C++

```
void RemoveUserInterface(
   System.string* ApiUuid
)
```

### C++/CLI

```cpp
void RemoveUserInterface(
   System.String^ ApiUuid
)
```

### Parameters

- `ApiUuid`: UUID of the add-in

## Examples

This code snippet shows how to remove an add-in's user interface from the DraftSight user interface (from the DraftSight API [COM native C++ template file](GettingStarted-draftsightapi.html) **DsAddinConnection.h**).

##### COM native C++

m_DsApp->RemoveUserInterface( m_sApiUuid );

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R1
