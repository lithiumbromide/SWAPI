---
title: "CreateGroup Method (IDocument)"
project: ""
interface: "IDocument"
member: "CreateGroup"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateGroup.html"
---

# CreateGroup Method (IDocument)

Creates an EntityGroup, which combines the specified entities into a group that you can manipulate in a single operation.

## Syntax

### Visual Basic

```vb
Function CreateGroup( _
   ByVal Name As System.String, _
   ByVal Unnamed As System.Boolean, _
   ByVal Description As System.String, _
   ByVal EntitiesArray As System.Object _
) As Group
```

### C#

```csharp
Group CreateGroup(
   System.string Name,
   System.bool Unnamed,
   System.string Description,
   System.object EntitiesArray
)
```

### JScript

```
function CreateGroup(
   Name : System.String,
   Unnamed : System.boolean,
   Description : System.String,
   EntitiesArray : System.Object
) : Group;
```

### Managed Extensions for C++

```
Group* CreateGroup(
   System.string* Name,
   System.bool Unnamed,
   System.string* Description,
   System.Object* EntitiesArray
)
```

### C++/CLI

```cpp
Group^ CreateGroup(
   System.String^ Name,
   System.bool Unnamed,
   System.String^ Description,
   System.Object^ EntitiesArray
)
```

### Parameters

- `Name`: Name for the EntityGroup
- `Unnamed`: True to create an anonymous EntityGroup, false to use Name for the EntityGroup
- `Description`: Description of the EntityGroup or an empty string
- `EntitiesArray`: Array of entities

### Return Value

[Group](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetGroup Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetGroup.html)
[IDocument::GetGroups Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetGroups.html)

## Availability

DraftSight V1R4.0
