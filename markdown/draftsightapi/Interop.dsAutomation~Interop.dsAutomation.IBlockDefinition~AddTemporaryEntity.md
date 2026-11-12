---
title: "AddTemporaryEntity Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "AddTemporaryEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~AddTemporaryEntity.html"
---

# AddTemporaryEntity Method (IBlockDefinition)

Inserts the specified temporary entity in the Block definition.

## Syntax

### Visual Basic

```vb
Sub AddTemporaryEntity( _
   ByVal Entity As System.Object _
)
```

### C#

```csharp
void AddTemporaryEntity(
   System.object Entity
)
```

### JScript

```
function AddTemporaryEntity(
   Entity : System.Object
);
```

### Managed Extensions for C++

```
void AddTemporaryEntity(
   System.Object* Entity
)
```

### C++/CLI

```cpp
void AddTemporaryEntity(
   System.Object^ Entity
)
```

### Parameters

- `Entity`: Temporary entity to insert in the Block definition

## Examples

[Add Temporary Entities to Block Definition (C#)](Add_Temporary_Entities_to_Block_Definition_Example_CSharp.htm)
[Add Temporary Entities to Block Definition (VB.NET)](Add_Temporary_Entities_to_Block_Definition_Example_VBNET.htm)
[Add Temporary Entities to Block Definition (VBA)](Add_Temporary_Entities_to_Block_Definition_Example_VBA.htm)

## Remarks

[Temporary entity mode](Interop.dsAutomation~Interop.dsAutomation.IApplication~TemporaryEntityMode.html) must be on to add temporary entities to the Block definition.

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IApplication::IsTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~IsTemporaryEntity.html)
[ISketchManager::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AddTemporaryEntity.html)
[ITracker::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ITracker~AddTemporaryEntity.html)

## Availability

DraftSight V1R4.0
