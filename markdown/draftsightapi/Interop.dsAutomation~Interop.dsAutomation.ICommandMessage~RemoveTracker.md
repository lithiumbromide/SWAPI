---
title: "RemoveTracker Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "RemoveTracker"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~RemoveTracker.html"
---

# RemoveTracker Method (ICommandMessage)

Removes the tracker, the mechanism that draws temporary entities along the cursor's path when prompting a user for a value, keyword, or selection.

## Syntax

### Visual Basic

```vb
Sub RemoveTracker( _
   ByVal Tracker As Tracker _
)
```

### C#

```csharp
void RemoveTracker(
   Tracker Tracker
)
```

### JScript

```
function RemoveTracker(
   Tracker : Tracker
);
```

### Managed Extensions for C++

```
void RemoveTracker(
   Tracker* Tracker
)
```

### C++/CLI

```cpp
void RemoveTracker(
   Tracker^ Tracker
)
```

### Parameters

- `Tracker`: [Tracker](Interop.dsAutomation~Interop.dsAutomation.ITracker.html) to remove from the drawing

## Examples

[Create Tracker (C#)](Create_Tracker_Example_CSharp.htm)
[Create Tracker (VB.NET)](Create_Tracker_Example_VBNET.htm)
[Create Tracker (VBA)](Create_Tracker_Example_VBA.htm)

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[IApplication::CreateTracker Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateTracker.html)
[ICommandMessage::AddTracker Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~AddTracker.html)

## Availability

DraftSight V1R4.0
