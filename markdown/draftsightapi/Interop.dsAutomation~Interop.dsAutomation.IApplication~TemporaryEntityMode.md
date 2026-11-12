---
title: "TemporaryEntityMode Property (IApplication)"
project: ""
interface: "IApplication"
member: "TemporaryEntityMode"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~TemporaryEntityMode.html"
---

# TemporaryEntityMode Property (IApplication)

Gets or sets temporary entity mode on or off.

## Syntax

### Visual Basic

```vb
Property TemporaryEntityMode As System.Boolean
```

### C#

```csharp
System.bool TemporaryEntityMode {get; set;}
```

### JScript

```
function get,set TemporaryEntityMode : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_TemporaryEntityMode();
__property void set_TemporaryEntityMode(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool TemporaryEntityMode {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to set temporary entity mode on, false to set temporary entity mode off

## Examples

[Create Tracker (C#)](Create_Tracker_Example_CSharp.htm)
[Create Tracker (VB.NET)](Create_Tracker_Example_VBNET.htm)
[Create Tracker (VBA)](Create_Tracker_Example_VBA.htm)
[Add Temporary Entities to Block Definition (C#)](Add_Temporary_Entities_to_Block_Definition_Example_CSharp.htm)
[Add Temporary Entities to Block Definition (VB.NET)](Add_Temporary_Entities_to_Block_Definition_Example_VBNET.htm)
[Add Temporary Entities to Block Definition (VBA)](Add_Temporary_Entities_to_Block_Definition_Example_VBA.htm)

## Remarks

When temporary entity mode is on, then temporary entities are added to the drawing database.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::IsTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~IsTemporaryEntity.html)
[IBlockDefinition::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~AddTemporaryEntity.html)
[ISketchManager::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~AddTemporaryEntity.html)
[ITracker::AddTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ITracker~AddTemporaryEntity.html)
[ITracker::RemoveTemporaryEntity Method ()](Interop.dsAutomation~Interop.dsAutomation.ITracker~RemoveTemporaryEntity.html)

## Availability

DraftSight V1R4.0
