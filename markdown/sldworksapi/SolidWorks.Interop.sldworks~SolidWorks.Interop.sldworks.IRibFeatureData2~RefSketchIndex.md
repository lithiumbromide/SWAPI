---
title: "RefSketchIndex Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "RefSketchIndex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~RefSketchIndex.html"
---

# RefSketchIndex Property (IRibFeatureData2)

Gets or sets which sketch segment defines the draft direction of the rib feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property RefSketchIndex As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Integer

instance.RefSketchIndex = value

value = instance.RefSketchIndex
```

### C#

```csharp
System.int RefSketchIndex {get; set;}
```

### C++/CLI

```cpp
property System.int RefSketchIndex {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Index of the sketch segment that defines the draft direction

## VBA Syntax

See [RibFeatureData2::RefSketchIndex](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~RefSketchIndex.html).

## Remarks

This property is valid only when [IRibFeatureData2::EnableDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~EnableDraft.html) is set to true.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)
[IRibFeatureData2::DraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftAngle.html)
[IRibFeatureData2::DraftOutward Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftOutward.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
