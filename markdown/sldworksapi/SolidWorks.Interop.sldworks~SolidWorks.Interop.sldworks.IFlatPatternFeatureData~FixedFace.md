---
title: "FixedFace Property (IFlatPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFlatPatternFeatureData"
member: "FixedFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~FixedFace.html"
---

# FixedFace Property (IFlatPatternFeatureData)

Obsolete. Superseded by [IFlatPatternFeatureData::FixedFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlatPatternFeatureData~FixedFace2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedFace As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFlatPatternFeatureData
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

See [FlatPatternFeatureData::FixedFace](ms-its:sldworksapivb6.chm::/sldworks~FlatPatternFeatureData~FixedFace.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.html)
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
