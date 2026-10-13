---
title: "PreLoadForceValue Property (ICWGeneralSpringConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGeneralSpringConnector"
member: "PreLoadForceValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~PreLoadForceValue.html"
---

# PreLoadForceValue Property (ICWGeneralSpringConnector)

Gets or sets the preload force value.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreLoadForceValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGeneralSpringConnector
Dim value As System.Double

instance.PreLoadForceValue = value

value = instance.PreLoadForceValue
```

### C#

```csharp
System.double PreLoadForceValue {get; set;}
```

### C++/CLI

```cpp
property System.double PreLoadForceValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Preload force value in Newtons

## VBA Syntax

See [CWGeneralSpringConnector::PreLoadForceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGeneralSpringConnector~PreLoadForceValue.html).

## Examples

See the [ICWGeneralSpringConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html) examples.

## Remarks

Specify the units of this property with [ICWGeneralSpringConnector::Unit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~Unit.html).

Use [ICWGeneralSpringConnector::PreLoadForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector~PreLoadForceType.html) to specify the preload force type.

## See Also

[ICWGeneralSpringConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector.html)
[ICWGeneralSpringConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGeneralSpringConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2025 SP0
