---
title: "Reverse Property (IGearMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGearMateFeatureData"
member: "Reverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData~Reverse.html"
---

# Reverse Property (IGearMateFeatureData)

Gets or sets whether to change the direction of rotation of the gears relative to one another in this gear mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGearMateFeatureData
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

True to reverse the direction of rotation, false to not

## VBA Syntax

See [GearMateFeatureData::Reverse](ms-its:sldworksapivb6.chm::/sldworks~GearMateFeatureData~Reverse.html).

## Examples

See the [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html) example.

## See Also

[IGearMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html)
[IGearMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
