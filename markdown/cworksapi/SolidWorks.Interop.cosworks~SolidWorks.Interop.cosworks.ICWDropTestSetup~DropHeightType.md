---
title: "DropHeightType Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "DropHeightType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~DropHeightType.html"
---

# DropHeightType Property (ICWDropTestSetup)

Gets or sets the drop height type.

## Syntax

### Visual Basic (Declaration)

```vb
Property DropHeightType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.DropHeightType = value

value = instance.DropHeightType
```

### C#

```csharp
System.int DropHeightType {get; set;}
```

### C++/CLI

```cpp
property System.int DropHeightType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Drop height type as defined in [swsDropHeightType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropHeightType_e.html) (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::DropHeightType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~DropHeightType.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This property is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_DropHeight.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
