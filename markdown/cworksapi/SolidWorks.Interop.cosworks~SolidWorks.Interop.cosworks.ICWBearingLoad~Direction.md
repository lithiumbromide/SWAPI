---
title: "Direction Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "Direction"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~Direction.html"
---

# Direction Property (ICWBearingLoad)

Gets or sets the direction of this bearing load in the selected coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Integer

instance.Direction = value

value = instance.Direction
```

### C#

```csharp
System.int Direction {get; set;}
```

### C++/CLI

```cpp
property System.int Direction {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 for X direction, 1 for Y direction

## VBA Syntax

See [CWBearingLoad::Direction](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~Direction.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::XDirectionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionValue.html)
[ICWBearingLoad::YDirectionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~YDirectionValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
