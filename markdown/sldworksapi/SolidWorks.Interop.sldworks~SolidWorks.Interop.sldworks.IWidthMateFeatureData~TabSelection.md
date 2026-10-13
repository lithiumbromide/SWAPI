---
title: "TabSelection Property (IWidthMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWidthMateFeatureData"
member: "TabSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~TabSelection.html"
---

# TabSelection Property (IWidthMateFeatureData)

Gets or sets the tab references for this width mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property TabSelection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWidthMateFeatureData
Dim value As System.Object

instance.TabSelection = value

value = instance.TabSelection
```

### C#

```csharp
System.object TabSelection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TabSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of tab entities (see **Remarks**)

## VBA Syntax

See [WidthMateFeatureData::TabSelection](ms-its:sldworksapivb6.chm::/sldworks~WidthMateFeatureData~TabSelection.html).

## Remarks

The tab entities can include:

- Two parallel planar [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
- Two non-parallel planar faces
- One cylindrical face or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)

## See Also

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html)
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
