---
title: "MLeaderStyle Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "MLeaderStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~MLeaderStyle.html"
---

# MLeaderStyle Property (IMLeader)

Gets or sets the name of the MultiLeaderStyle.

## Syntax

### Visual Basic

```vb
Property MLeaderStyle As System.String
```

### C#

```csharp
System.string MLeaderStyle {get; set;}
```

### JScript

```
function get,set MLeaderStyle : System.String
```

### Managed Extensions for C++

```
__property System.string* get_MLeaderStyle();
__property void set_MLeaderStyle(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ MLeaderStyle {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of MultiLeaderStyle, "Standard" or "Annotative"

## Remarks

Other multileader styles may be available. Check the DraftSight user interface.

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
