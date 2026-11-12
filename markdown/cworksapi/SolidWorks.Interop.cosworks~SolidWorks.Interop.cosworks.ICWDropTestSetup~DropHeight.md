---
title: "DropHeight Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "DropHeight"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~DropHeight.html"
---

# DropHeight Property (ICWDropTestSetup)

Gets or sets the height from which the model is dropped to the floor.

## Syntax

### Visual Basic (Declaration)

```vb
Property DropHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.DropHeight = value

value = instance.DropHeight
```

### C#

```csharp
System.double DropHeight {get; set;}
```

### C++/CLI

```cpp
property System.double DropHeight {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Height of drop (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::DropHeight](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~DropHeight.html).

## Examples

See the [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html) examples.

## Remarks

This property is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_DropHeight.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
