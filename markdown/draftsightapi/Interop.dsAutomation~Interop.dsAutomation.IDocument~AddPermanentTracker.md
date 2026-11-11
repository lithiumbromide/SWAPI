---
title: "AddPermanentTracker Method (IDocument)"
project: ""
interface: "IDocument"
member: "AddPermanentTracker"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~AddPermanentTracker.html"
---

# AddPermanentTracker Method (IDocument)

Adds a permanent tracker to this document.

## Syntax

### Visual Basic

```vb
Sub AddPermanentTracker( _
   ByVal Tracker As Tracker _
)
```

### C#

```csharp
void AddPermanentTracker(
   Tracker Tracker
)
```

### JScript

```
function AddPermanentTracker(
   Tracker : Tracker
);
```

### Managed Extensions for C++

```
void AddPermanentTracker(
   Tracker* Tracker
)
```

### C++/CLI

```cpp
void AddPermanentTracker(
   Tracker^ Tracker
)
```

### Parameters

- `Tracker`: [Tracker](Interop.dsAutomation~Interop.dsAutomation.ITracker.html) to add to this document

## Remarks

Unlike [ICommandMessage::AddTracker](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~AddTracker.html), this method adds a permanent tracker that displays all the time, not just during command workflows. The permanent tracker can be an XYZ tripod or the mouse cursor.

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::RemovePermanentTracker Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemovePermanentTracker.html)
[IApplication::CreateTracker Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateTracker.html)

## Availability

DraftSight 2020 SP0
