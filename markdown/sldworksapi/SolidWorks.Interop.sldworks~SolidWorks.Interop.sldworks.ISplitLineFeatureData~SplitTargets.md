---
title: "SplitTargets Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "SplitTargets"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTargets.html"
---

# SplitTargets Property (ISplitLineFeatureData)

Gets or sets the faces or bodies to split.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitTargets As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Object

instance.SplitTargets = value

value = instance.SplitTargets
```

### C#

```csharp
System.object SplitTargets {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SplitTargets {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [SplitLineFeatureData::SplitTargets](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~SplitTargets.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::GetSplitTargetsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitTargetsCount.html)
[ISplitLineFeatureData::IGetSplitTargets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTargets.html)
[ISplitLineFeatureData::ISetSplitTargets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTargets.html)
[ISplitLineFeatureData::SplitAll Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitAll.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
