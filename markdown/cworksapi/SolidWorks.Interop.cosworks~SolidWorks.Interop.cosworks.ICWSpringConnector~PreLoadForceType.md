---
title: "PreLoadForceType Property (ICWSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpringConnector"
member: "PreLoadForceType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~PreLoadForceType.html"
---

# PreLoadForceType Property (ICWSpringConnector)

Gets or sets the preload force type.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreLoadForceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpringConnector
Dim value As System.Integer

instance.PreLoadForceType = value

value = instance.PreLoadForceType
```

### C#

```csharp
System.int PreLoadForceType {get; set;}
```

### C++/CLI

```cpp
property System.int PreLoadForceType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Preload force type as defined in [swsPreloadForceType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPreLoadForceType_e.html)

## VBA Syntax

See [CWSpringConnector::PreLoadForceType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpringConnector~PreLoadForceType.html).

## Examples

See the [ICWSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html) examples.

## See Also

[ICWSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector.html)
[ICWSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector_members.html)
[ICWSpringConnector::PreLoadForceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpringConnector~PreLoadForceValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
