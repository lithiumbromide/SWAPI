---
title: "IGroup Interface"
project: ""
interface: "IGroup"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup.html"
---

# IGroup Interface

Allows access to an EntityGroup, which contains entities that have been combined into a group that you can manipulate in a single operation (e.g., moving, rotating, mirroring, or scaling).

## Syntax

### Visual Basic

```vb
Public Interface IGroup
```

### C#

```csharp
public interface IGroup
```

### JScript

```
public interface IGroup
```

### Managed Extensions for C++

```
public __gc __interface IGroup
```

### C++/CLI

```cpp
public interface class IGroup
```

## Examples

[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## Remarks

Only top-level entities in model or sheet space can be in EntityGroups. Entities can belong to multiple EntityGroups.

## Accessors

[IDocument::CreateGroup](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateGroup.html)

[IDocument::GetGroup](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetGroup.html)

[IDocument::GetGroups](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetGroups.html)

[IDocument::GetObjectByHandle](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetObjectByHandle.html)

[ISelectionManager::GetSelectedObject](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)

[ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)

[ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html)

## Access Diagram

DSObjectModel.pdf#Group

[Group](DSObjectModel.pdf#Group)

## See Also

[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
