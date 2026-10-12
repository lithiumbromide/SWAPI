---
title: "XDirectionReverse2 Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "XDirectionReverse2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionReverse2.html"
---

# XDirectionReverse2 Property (ICWBearingLoad)

Gets or sets whether to reverse the X direction of this bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Property XDirectionReverse2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Boolean

instance.XDirectionReverse2 = value

value = instance.XDirectionReverse2
```

### C#

```csharp
System.bool XDirectionReverse2 {get; set;}
```

### C++/CLI

```cpp
property System.bool XDirectionReverse2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to reverse the X direction, 0 or false to not

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
