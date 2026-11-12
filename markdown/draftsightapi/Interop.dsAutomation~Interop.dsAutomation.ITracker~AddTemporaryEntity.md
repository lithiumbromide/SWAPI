---
title: "AddTemporaryEntity Method (ITracker)"
project: ""
interface: "ITracker"
member: "AddTemporaryEntity"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITracker~AddTemporaryEntity.html"
---

# AddTemporaryEntity Method (ITracker)

Adds the specified temporary entity to be drawn by the tracker.

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

- `Entity`: Temporary entity to be drawn by the tracker

## Examples

[Create Tracker (C#)](Create_Tracker_Example_CSharp.htm)
[Create Tracker (VB.NET)](Create_Tracker_Example_VBNET.htm)
[Create Tracker (VBA)](Create_Tracker_Example_VBA.htm)

## Remarks

[Temporary entity mode](Interop.dsAutomation~Interop.dsAutomation.IApplication~TemporaryEntityMode.html) must be on to draw temporary entities along the cursor.

## See Also

[ITracker Interface](Interop.dsAutomation~Interop.dsAutomation.ITracker.html)
[ITracker Members](Interop.dsAutomation~Interop.dsAutomation.ITracker_members.html)
[ITracker::RemoveTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ITracker~RemoveTemporaryEntity.html)
[IApplication::IsTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~IsTemporaryEntity.html)
[IBlockDefinition::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~AddTemporaryEntity.html)
[ISketchManager::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AddTemporaryEntity.html)

## Availability

DraftSight V1R4.0
