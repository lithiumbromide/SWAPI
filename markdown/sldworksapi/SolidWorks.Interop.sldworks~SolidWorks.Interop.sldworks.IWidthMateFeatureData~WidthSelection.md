---
title: "WidthSelection Property (IWidthMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWidthMateFeatureData"
member: "WidthSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~WidthSelection.html"
---

# WidthSelection Property (IWidthMateFeatureData)

Gets or sets the width references for this width mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property WidthSelection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWidthMateFeatureData
Dim value As System.Object

instance.WidthSelection = value

value = instance.WidthSelection
```

### C#

```csharp
System.object WidthSelection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ WidthSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of planar [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) (see **Remarks**)

## VBA Syntax

See [WidthMateFeatureData::WidthSelection](ms-its:sldworksapivb6.chm::/sldworks~WidthMateFeatureData~WidthSelection.html).

## Remarks

The planar faces can include:

- Two parallel planar faces
- Two non-parallel planar faces

## See Also

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html)
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
