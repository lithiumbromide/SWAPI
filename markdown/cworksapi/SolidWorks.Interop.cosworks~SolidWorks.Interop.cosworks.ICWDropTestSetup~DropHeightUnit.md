---
title: "DropHeightUnit Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "DropHeightUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~DropHeightUnit.html"
---

# DropHeightUnit Property (ICWDropTestSetup)

Gets or sets the units of drop height.

## Syntax

### Visual Basic (Declaration)

```vb
Property DropHeightUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.DropHeightUnit = value

value = instance.DropHeightUnit
```

### C#

```csharp
System.int DropHeightUnit {get; set;}
```

### C++/CLI

```cpp
property System.int DropHeightUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html) (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::DropHeightUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~DropHeightUnit.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This property is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_DropHeight.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
