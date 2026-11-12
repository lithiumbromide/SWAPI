---
title: "DropType Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "DropType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~DropType.html"
---

# DropType Property (ICWDropTestSetup)

Gets or sets the type of input to specify for this drop test setup.

## Syntax

### Visual Basic (Declaration)

```vb
Property DropType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

instance.DropType = value

value = instance.DropType
```

### C#

```csharp
System.int DropType {get; set;}
```

### C++/CLI

```cpp
property System.int DropType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Drop test setup input type as defined in [swsDropType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropType_e.html)

## VBA Syntax

See [CWDropTestSetup::DropType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~DropType.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
