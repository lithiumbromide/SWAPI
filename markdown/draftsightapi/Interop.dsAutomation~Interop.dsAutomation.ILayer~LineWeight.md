---
title: "LineWeight Property (ILayer)"
project: ""
interface: "ILayer"
member: "LineWeight"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~LineWeight.html"
---

# LineWeight Property (ILayer)

Gets or sets the LineWeight for the Layer.

## Syntax

### Visual Basic

```vb
Property LineWeight As dsLineWeight_e
```

### C#

```csharp
dsLineWeight_e LineWeight {get; set;}
```

### JScript

```
function get,set LineWeight : dsLineWeight_e
```

### Managed Extensions for C++

```
__property dsLineWeight_e get_LineWeight();
__property void set_LineWeight(
   dsLineWeight_e value
);
```

### C++/CLI

```cpp
property dsLineWeight_e LineWeight {
   dsLineWeight_e get();
   void set (    dsLineWeight_e value);
}
```

### Property Value

LineWeight as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetLineWeightInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineWeightInViewport.html)
[ILayer::SetLineWeightInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetLineWeightInViewport.html)
[ILayer::RemoveLineWeightOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverride.html)
[ILayer::RemoveLineWeightOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverrides.html)

## Availability

DraftSight V1R1.1
