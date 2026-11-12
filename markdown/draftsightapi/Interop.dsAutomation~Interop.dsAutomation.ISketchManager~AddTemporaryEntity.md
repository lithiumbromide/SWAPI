---
title: "AddTemporaryEntity Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "AddTemporaryEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AddTemporaryEntity.html"
---

# AddTemporaryEntity Method (ISketchManager)

Inserts the specified temporary entity in the drawing.

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

- `Entity`: Temporary entity to insert in the drawing

## Examples

[Create Tracker (C#)](Create_Tracker_Example_CSharp.htm)
[Create Tracker (VB.NET)](Create_Tracker_Example_VBNET.htm)
[Create Tracker (VBA)](Create_Tracker_Example_VBA.htm)

## Remarks

[Temporary entity mode](Interop.dsAutomation~Interop.dsAutomation.IApplication~TemporaryEntityMode.html) must be on to add temporary entities to the drawing.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[IApplication::IsTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~IsTemporaryEntity.html)
[IBlockDefinition::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~AddTemporaryEntity.html)
[ITracker::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ITracker~AddTemporaryEntity.html)

## Availability

DraftSight V1R4.0
