---
title: "Direction Property (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Direction.html"
---

# Direction Property (IDomeFeatureData2)

Gets or sets the direction of the dome feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Direction As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim value As System.Object

instance.Direction = value

value = instance.Direction
```

### C#

```csharp
System.object Direction {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Edge indicating the direction of dome feature

## VBA Syntax

See [DomeFeatureData2::Direction](ms-its:sldworksapivb6.chm::/sldworks~DomeFeatureData2~Direction.html).

## Examples

[Get and Set Direction for Dome Feature (VBA)](Get_and_Set_Direction_for_Dome_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
