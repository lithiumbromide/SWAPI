---
title: "CloseDocument Method (IApplication)"
project: ""
interface: "IApplication"
member: "CloseDocument"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CloseDocument.html"
---

# CloseDocument Method (IApplication)

Closes the specified document.

## Syntax

### Visual Basic

```vb
Sub CloseDocument( _
   ByVal PathName As System.String, _
   ByVal SaveChanges As System.Boolean _
)
```

### C#

```csharp
void CloseDocument(
   System.string PathName,
   System.bool SaveChanges
)
```

### JScript

```
function CloseDocument(
   PathName : System.String,
   SaveChanges : System.boolean
);
```

### Managed Extensions for C++

```
void CloseDocument(
   System.string* PathName,
   System.bool SaveChanges
)
```

### C++/CLI

```cpp
void CloseDocument(
   System.String^ PathName,
   System.bool SaveChanges
)
```

### Parameters

- `PathName`: Path and file name of the document to close
- `SaveChanges`: True to save the changes made to the specified document, false to discard the changes

## Examples

[Fire Application and Document Events (C#)](Fire_Application_and_Document_Events_Example_CSharp.htm)
[Fire Application and Document Events (VB.NET)](Fire_Application_and_Document_Events_Example_VBNET.htm)
[Fire Application and Document Events (VBA)](Fire_Application_and_Document_Events_Example_VBA.htm)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetActiveDocument Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveDocument.html)
[IApplication::GetDocuments Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetDocuments.html)
[IApplication::OpenDocument Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenDocument.html)

## Availability

DraftSight V1R1
