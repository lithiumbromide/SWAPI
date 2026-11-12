---
title: "BodiesToCombine Property (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "BodiesToCombine"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~BodiesToCombine.html"
---

# BodiesToCombine Property (ICombineBodiesFeatureData)

Gets or sets the bodies to combine.

## Syntax

### Visual Basic (Declaration)

```vb
Property BodiesToCombine As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData
Dim value As System.Object

instance.BodiesToCombine = value

value = instance.BodiesToCombine
```

### C#

```csharp
System.object BodiesToCombine {get; set;}
```

### C++/CLI

```cpp
property System.Object^ BodiesToCombine {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [CombineBodiesFeatureData::BodiesToCombine](ms-its:sldworksapivb6.chm::/sldworks~CombineBodiesFeatureData~BodiesToCombine.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)
[ICombineBodiesFeatureData::GetBodiesToCombineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~GetBodiesToCombineCount.html)
[ICombineBodiesFeatureData::IGetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~IGetBodiesToCombine.html)
[ICombineBodiesFeatureData::ISetBodiesToCombine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~ISetBodiesToCombine.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
