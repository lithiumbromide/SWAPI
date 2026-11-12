---
title: "AddTracker Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "AddTracker"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~AddTracker.html"
---

# AddTracker Method (ICommandMessage)

Adds a tracker, the mechanism that replaces the cursor with a temporary entity when prompting a user for a value, keyword, or selection.

## Syntax

### Visual Basic

```vb
Sub AddTracker( _
   ByVal Tracker As Tracker _
)
```

### C#

```csharp
void AddTracker(
   Tracker Tracker
)
```

### JScript

```
function AddTracker(
   Tracker : Tracker
);
```

### Managed Extensions for C++

```
void AddTracker(
   Tracker* Tracker
)
```

### C++/CLI

```cpp
void AddTracker(
   Tracker^ Tracker
)
```

### Parameters

- `Tracker`: [Tracker](Interop.dsAutomation~Interop.dsAutomation.ITracker.html) to add to the drawing

## Examples

[Create Tracker (C#)](Create_Tracker_Example_CSharp.htm)
[Create Tracker (VB.NET)](Create_Tracker_Example_VBNET.htm)
[Create Tracker (VBA)](Create_Tracker_Example_VBA.htm)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[IApplication::CreateTracker Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateTracker.html)
[ITracker::RemoveTracker Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~RemoveTracker.html)

## Availability

DraftSight V1R4.0
