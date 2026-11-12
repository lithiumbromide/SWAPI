---
title: "ReverseDirection Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ReverseDirection.html"
---

# ReverseDirection Property (IDraftFeatureData2)

Gets or sets whether the direction of the draft feature is reversed.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the direction of the draft feature, false does not

## VBA Syntax

See [DraftFeatureData2::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~ReverseDirection.html).

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
