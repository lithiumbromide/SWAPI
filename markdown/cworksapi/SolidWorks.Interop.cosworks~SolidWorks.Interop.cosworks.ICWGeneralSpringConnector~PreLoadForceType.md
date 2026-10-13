---
title: "PreLoadForceType Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "PreLoadForceType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~PreLoadForceType.html"
---

# PreLoadForceType Property (ICWGeneralSpringConnector)

Gets or sets the type of preload force.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreLoadForceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
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

Type of preload force (see **Remarks**)

## VBA Syntax

See [CWGeneralSpringConnector::PreLoadForceType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~PreLoadForceType.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

0 = Compression preload force

1 = Tension preload force

Use [ICWGeneralSpringConnector::PreLoadForceValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~PreLoadForceValue.html) to specify the force.

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
