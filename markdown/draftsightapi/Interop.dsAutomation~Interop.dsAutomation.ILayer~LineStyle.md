---
title: "LineStyle Property (ILayer)"
project: ""
interface: "ILayer"
member: "LineStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~LineStyle.html"
---

# LineStyle Property (ILayer)

Gets or sets the name of the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) for the Layer.

## Syntax

### Visual Basic

```vb
Property LineStyle As System.String
```

### C#

```csharp
System.string LineStyle {get; set;}
```

### JScript

```
function get,set LineStyle : System.String
```

### Managed Extensions for C++

```
__property System.string* get_LineStyle();
__property void set_LineStyle(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ LineStyle {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the LineStyle for the Layer

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetLineSyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineSyleInViewport.html)
[ILayer::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverride.html)
[ILayer::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverrides.html)
[ILayer::SetLineStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetLineStyleInViewport.html)

## Availability

DraftSight V1R1.1
