---
title: "LeaderAnchorStyle Property (IPMIDatumFeature)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumFeature"
member: "LeaderAnchorStyle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature~LeaderAnchorStyle.html"
---

# LeaderAnchorStyle Property (IPMIDatumFeature)

Gets the PMI datum leader anchor style.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderAnchorStyle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumFeature
Dim value As System.Integer

instance.LeaderAnchorStyle = value

value = instance.LeaderAnchorStyle
```

### C#

```csharp
System.int LeaderAnchorStyle {get; set;}
```

### C++/CLI

```cpp
property System.int LeaderAnchorStyle {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

PMI datum leader anchor style as defined in [swPMIDatumAnchorStyle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumAnchorStyle_e.html)

## VBA Syntax

See [PMIDatumFeature::LeaderAnchorStyle](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumFeature~LeaderAnchorStyle.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.html)
[IPMIDatumFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
