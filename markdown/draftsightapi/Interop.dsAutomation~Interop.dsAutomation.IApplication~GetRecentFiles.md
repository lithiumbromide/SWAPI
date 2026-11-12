---
title: "GetRecentFiles Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetRecentFiles"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRecentFiles.html"
---

# GetRecentFiles Method (IApplication)

Gets the paths and file names of the files most recently opened in DraftSight.

## Syntax

### Visual Basic

```vb
Sub GetRecentFiles( _
   ByRef FilesStrArray As System.Object _
)
```

### C#

```csharp
void GetRecentFiles(
   out System.object FilesStrArray
)
```

### JScript

```
function GetRecentFiles(
   FilesStrArray : System.Object
);
```

### Managed Extensions for C++

```
void GetRecentFiles(
   [PARAMFLAG::Out] System.Object* FilesStrArray
)
```

### C++/CLI

```cpp
void GetRecentFiles(
   [Out] System.Object^ FilesStrArray
)
```

### Parameters

- `FilesStrArray`: Array of strings of the paths and file names of the files most recently opened in DraftSight

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R6.0
