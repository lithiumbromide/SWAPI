---
title: "SelectedPoint Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "SelectedPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~SelectedPoint.html"
---

# SelectedPoint Property (ILocalCurvePatternFeatureData)

Gets or sets the reference point for this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectedPoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object

instance.SelectedPoint = value

value = instance.SelectedPoint
```

### C#

```csharp
System.object SelectedPoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectedPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference point (see **Remarks**)

## VBA Syntax

See [LocalCurvePatternFeatureData::SelectedPoint](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~SelectedPoint.html).

## Remarks

You can pre-select the reference point using Mark = 32 before creating the feature definition.

This property is valid only if [ILocalCurvePatternFeatureData::D1ReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.html) is set to [swLocalCurvePatternReferencePoint_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalCurvePatternReferencePoint_e.html).swLocalCurvePatternSelectedPoint.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Curve Driven Component Pattern** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
