---
title: "XDirectionValue Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "XDirectionValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionValue.html"
---

# XDirectionValue Property (ICWBearingLoad)

Gets or sets the value of the bearing load in the X direction of the selected coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Property XDirectionValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Double

instance.XDirectionValue = value

value = instance.XDirectionValue
```

### C#

```csharp
System.double XDirectionValue {get; set;}
```

### C++/CLI

```cpp
property System.double XDirectionValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Value of the bearing load in the X direction of the selected coordinate system

## VBA Syntax

See [CWBearingLoad::XDirectionValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~XDirectionValue.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::YDirectionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~YDirectionValue.html)
[ICWBearingLoad::Direction Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~Direction.html)
[ICWBearingLoad::XDirectionReverse Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionReverse.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
