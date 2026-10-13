---
title: "FixedPoint Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "FixedPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixedPoint.html"
---

# FixedPoint Property (IJogFeatureData)

Gets or sets the fixed point x, y, z coordinates for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedPoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Object

instance.FixedPoint = value

value = instance.FixedPoint
```

### C#

```csharp
System.object FixedPoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FixedPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of fixed point coordinates

## VBA Syntax

See [JogFeatureData::FixedPoint](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~FixedPoint.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::IGetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~IGetFixedPoint.html)
[IJogFeatureData::ISetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ISetFixedPoint.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
