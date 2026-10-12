---
title: "FeatureManagerSplitterPosition Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureManagerSplitterPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureManagerSplitterPosition.html"
---

# FeatureManagerSplitterPosition Property (IModelDoc2)

Splits the FeatureManager design tree and gets or sets the location of the split bar in the FeatureManager design tree panel.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureManagerSplitterPosition As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Double

instance.FeatureManagerSplitterPosition = value

value = instance.FeatureManagerSplitterPosition
```

### C#

```csharp
System.double FeatureManagerSplitterPosition {get; set;}
```

### C++/CLI

```cpp
property System.double FeatureManagerSplitterPosition {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Percentage value between 0 and 1, which sets the location of the split bar in the FeatureManager design tree panel and the size of each split FeatureManager design tree (see **Remarks**)

## VBA Syntax

See [ModelDoc2::FeatureManagerSplitterPosition](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureManagerSplitterPosition.html).

## Examples

[Add ActiveX Tabs to FeatureManager Design Tree (C#)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_CSharp.htm)
[Add ActiveX Tabs to FeatureManager Design Tree (VB.NET)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VBNET.htm)
[Add ActiveX Tabs to FeatureManager Design Tree (VBA)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VB.htm)
[Split FeatureManager Design Tree and Position Splitter (C#)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_CSharp.htm)
[Split FeatureManager Design Tree and Position Splitter (VB.NET)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VBNET.htm)
[Split FeatureManager Design Tree and Position Splitter (VBA)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VB.htm)

## Remarks

| Setting this property to... | Results in the split panel bar.. . |
| --- | --- |
| 0 | Remaining above the FeatureManager design tree. |
| 1 | Moving below the FeatureManager design tree. |
| >0 and <1 | Setting the size of the split FeatureManager design trees within the FeatureManager design tree panel. For example, if you specify: 0.5, then each FeatureManager design tree takes up 50 percent of the panel, and the split bar is located between them. 0.8, then the bottom FeatureManager design tree takes up 80 percent of the panel, the top FeatureManager design tree takes up 20 percent of the panel, and the split bar is located between them. |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
