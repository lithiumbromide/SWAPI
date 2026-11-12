---
title: "NeutralPlane Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "NeutralPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~NeutralPlane.html"
---

# NeutralPlane Property (IDraftFeatureData2)

Gets or sets the neutral plane for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property NeutralPlane As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Object

instance.NeutralPlane = value

value = instance.NeutralPlane
```

### C#

```csharp
System.object NeutralPlane {get; set;}
```

### C++/CLI

```cpp
property System.Object^ NeutralPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Face to serve as the neutral plane

## VBA Syntax

See [DraftFeatureData2::NeutralPlane](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~NeutralPlane.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
