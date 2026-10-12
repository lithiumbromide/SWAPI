---
title: "SplitTools Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "SplitTools"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTools.html"
---

# SplitTools Property (ISplitLineFeatureData)

Gets or sets the tools used to make the split.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitTools As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Object

instance.SplitTools = value

value = instance.SplitTools
```

### C#

```csharp
System.object SplitTools {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SplitTools {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of tools used to make the split

## VBA Syntax

See [SplitLineFeatureData::SplitTools](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~SplitTools.html).

## Remarks

[Reference planes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html), [planar model faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), and [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) are valid tools for a split.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::GetSplitToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitToolsCount.html)
[ISplitLineFeatureData::IGetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTools.html)
[ISplitLineFeatureData::ISetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTools.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
