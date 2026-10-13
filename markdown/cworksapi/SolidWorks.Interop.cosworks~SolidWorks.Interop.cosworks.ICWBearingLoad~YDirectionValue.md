---
title: "YDirectionValue Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "YDirectionValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~YDirectionValue.html"
---

# YDirectionValue Property (ICWBearingLoad)

Gets or sets the value of the bearing load in the Y direction of the selected coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Property YDirectionValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Double

instance.YDirectionValue = value

value = instance.YDirectionValue
```

### C#

```csharp
System.double YDirectionValue {get; set;}
```

### C++/CLI

```cpp
property System.double YDirectionValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Value of the bearing load in the Y direction of the selected coordinate system

## VBA Syntax

See [CWBearingLoad::YDirectionValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~YDirectionValue.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::XDirectionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionValue.html)
[ICWBearingLoad::Direction Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~Direction.html)
[ICWBearingLoad::YDirectionReverse Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~YDirectionReverse.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
