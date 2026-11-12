---
title: "GetGroup Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetGroup"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetGroup.html"
---

# GetGroup Method (IDocument)

Gets the specified EntityGroup, which contains entities that have been combined into a group that you can manipulate in a single operation.

## Syntax

### Visual Basic

```vb
Function GetGroup( _
   ByVal Name As System.String _
) As Group
```

### C#

```csharp
Group GetGroup(
   System.string Name
)
```

### JScript

```
function GetGroup(
   Name : System.String
) : Group;
```

### Managed Extensions for C++

```
Group* GetGroup(
   System.string* Name
)
```

### C++/CLI

```cpp
Group^ GetGroup(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the EntityGroup

### Return Value

[EntityGroup](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CreateGroup Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateGroup.html)
[IDocument::GetGroups Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetGroups.html)

## Availability

DraftSight V1R4.0
