---
title: "Direction Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~Direction.html"
---

# Direction Property (ILoftedBendsFeatureData)

Gets or sets the thickness direction of this lofted bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean

instance.Direction = value

value = instance.Direction
```

### C#

```csharp
System.bool Direction {get; set;}
```

### C++/CLI

```cpp
property System.bool Direction {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the direction, false does not

## VBA Syntax

See [LoftedBendsFeatureData::Direction](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~Direction.html).

## Examples

See examples for [ILoftedBendsFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
