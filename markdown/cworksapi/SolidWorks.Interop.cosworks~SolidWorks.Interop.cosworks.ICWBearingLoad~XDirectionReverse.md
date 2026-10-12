---
title: "XDirectionReverse Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "XDirectionReverse"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionReverse.html"
---

# XDirectionReverse Property (ICWBearingLoad)

Obsolete. Superseded by [ICWBearingLoad::XDirectionReverse2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionReverse2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property XDirectionReverse As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Integer

instance.XDirectionReverse = value

value = instance.XDirectionReverse
```

### C#

```csharp
System.int XDirectionReverse {get; set;}
```

### C++/CLI

```cpp
property System.int XDirectionReverse {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse the X direction, 0 to not

## VBA Syntax

See [CWBearingLoad::XDirectionReverse](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~XDirectionReverse.html).

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)
[ICWBearingLoad::Direction Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~Direction.html)
[ICWBearingLoad::XDirectionValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~XDirectionValue.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
