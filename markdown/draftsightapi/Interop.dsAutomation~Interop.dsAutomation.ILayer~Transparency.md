---
title: "Transparency Property (ILayer)"
project: ""
interface: "ILayer"
member: "Transparency"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~Transparency.html"
---

# Transparency Property (ILayer)

Gets or sets the [transparency](Interop.dsAutomation~Interop.dsAutomation.ITransparency.html) percentage for this Layer.

## Syntax

### Visual Basic

```vb
Property Transparency As System.Integer
```

### C#

```csharp
System.int Transparency {get; set;}
```

### JScript

```
function get,set Transparency : System.int
```

### Managed Extensions for C++

```
__property System.int get_Transparency();
__property void set_Transparency(
   System.int value
);
```

### C++/CLI

```cpp
property System.int Transparency {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Transparency percentage (see **Remarks**)

## Examples

[Create Table (C#)](Create_Table_Example_CSharp.htm)
[Create Table (VB.NET)](Create_Table_Example_VBNET.htm)
[Create Table (VBA)](Create_Table_Example_VBA.htm)
[Create Table (JavaScript)](Create_Table_Example_JS.htm)

## Remarks

The transparency percentage is between 0 and 90 where 0 means no transparency (opaque).

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetTranparencyInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetTranparencyInViewport.html)
[ILayer::RemoveTransparencyOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverride.html)
[ILayer::RemoveTransparencyOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveTransparencyOverrides.html)
[ILayer::SetTranparencyInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetTranparencyInViewport.html)

## Availability

DraftSight V1R6.0
