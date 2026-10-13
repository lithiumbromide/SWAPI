---
title: "Reverse Property (IRackPinionMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRackPinionMateFeatureData"
member: "Reverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData~Reverse.html"
---

# Reverse Property (IRackPinionMateFeatureData)

Gets or sets whether to change the direction of movement of the rack and pinion relative to one another.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRackPinionMateFeatureData
Dim value As System.Boolean

instance.Reverse = value

value = instance.Reverse
```

### C#

```csharp
System.bool Reverse {get; set;}
```

### C++/CLI

```cpp
property System.bool Reverse {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of movement of the rack and pinion, false to not

## VBA Syntax

See [RackPinionMateFeatureData::Reverse](ms-its:sldworksapivb6.chm::/sldworks~RackPinionMateFeatureData~Reverse.html).

## Examples

See the [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html) example.

## See Also

[IRackPinionMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html)
[IRackPinionMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
