---
title: "DirectionPull Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "DirectionPull"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~DirectionPull.html"
---

# DirectionPull Property (IDraftFeatureData2)

Gets or sets the direction in which to pull this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectionPull As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Object

instance.DirectionPull = value

value = instance.DirectionPull
```

### C#

```csharp
System.object DirectionPull {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DirectionPull {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Face from which to pull this draft feature

## VBA Syntax

See [DraftFeatureData2::DirectionPull](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~DirectionPull.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
