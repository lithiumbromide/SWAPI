---
title: "FixedFace Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "FixedFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixedFace.html"
---

# FixedFace Property (IJogFeatureData)

Gets or sets the fixed face for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedFace As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Object

instance.FixedFace = value

value = instance.FixedFace
```

### C#

```csharp
System.object FixedFace {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FixedFace {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fixed [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [JogFeatureData::FixedFace](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~FixedFace.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
