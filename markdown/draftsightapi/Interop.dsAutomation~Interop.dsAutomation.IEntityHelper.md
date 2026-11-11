---
title: "IEntityHelper Interface"
project: ""
interface: "IEntityHelper"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html"
---

# IEntityHelper Interface

Allows access to entities.

## Syntax

### Visual Basic

```vb
Public Interface IEntityHelper
```

### C#

```csharp
public interface IEntityHelper
```

### JScript

```
public interface IEntityHelper
```

### Managed Extensions for C++

```
public __gc __interface IEntityHelper
```

### C++/CLI

```cpp
public interface class IEntityHelper
```

## Examples

[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)
[Select and Change Entities (JavaScript)](Select_and_Change_Entities_Example_JS.htm)
[Create and Change EntityGroups (C#)](Create_and_Change_EntityGroups_Example_CSharp.htm)
[Create and Change EntityGroups (VB.NET)](Create_and_Change_EntityGroups_Example_VBNET.htm)
[Create and Change EntityGroups (VBA)](Create_and_Change_EntityGroups_Example_VBA.htm)
[Create and Change EntityGroups (JavaScript)](Create_and_Change_EntityGroups_Example_JS.htm)

## Remarks

This interface allows you to access a group of sketch or BlockDefinition entities (Lines, Circles, Splines, etc.) and perform operations on those entities without having to cast each entity individually. Depending on what you want to do, call [ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html) or [ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html) or [IBlockDefinition::GetEntities](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetEntities.html) to create the group of entities on which to perform operations.

## Accessors

[IApplication::GetEntityHelper](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetEntityHelper.html)

## Access Diagram

DSObjectModel.pdf#EntityHelper

[EntityHelper](DSObjectModel.pdf#EntityHelper)

## See Also

[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
