---
title: "YDirectionReverse Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "YDirectionReverse"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~YDirectionReverse.html"
---

# YDirectionReverse Property (ICWBearingLoad)

Obsolete. Superseded by [ICWBearingLoad::YDirectionReverse2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~YDirectionReverse2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property YDirectionReverse As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Integer

instance.YDirectionReverse = value

value = instance.YDirectionReverse
```

### C#

```csharp
System.int YDirectionReverse {get; set;}
```

### C++/CLI

```cpp
property System.int YDirectionReverse {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse the Y direction, 0 to not

## VBA Syntax

See [CWBearingLoad::YDirectionReverse](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~YDirectionReverse.html).

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::YDirectionValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~YDirectionValue.html)
[ICWBearingLoad::Direction Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~Direction.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
