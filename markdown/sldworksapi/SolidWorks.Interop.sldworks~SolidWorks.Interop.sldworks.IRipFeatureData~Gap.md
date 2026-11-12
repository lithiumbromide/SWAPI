---
title: "Gap Property (IRipFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRipFeatureData"
member: "Gap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~Gap.html"
---

# Gap Property (IRipFeatureData)

Gets or sets the gap for this rip feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Gap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRipFeatureData
Dim value As System.Double

instance.Gap = value

value = instance.Gap
```

### C#

```csharp
System.double Gap {get; set;}
```

### C++/CLI

```cpp
property System.double Gap {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gap

## VBA Syntax

See [RipFeatureData::Gap](ms-its:sldworksapivb6.chm::/sldworks~RipFeatureData~Gap.html).

## Examples

See the [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html) examples.

## Remarks

| If... | Then SOLIDWORKS returns... |
| --- | --- |
| No value is set | 1 |
| Using the default gap | -1 |

## See Also

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.html)
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
