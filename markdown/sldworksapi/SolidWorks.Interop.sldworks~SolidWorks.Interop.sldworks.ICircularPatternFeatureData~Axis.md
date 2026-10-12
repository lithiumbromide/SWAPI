---
title: "Axis Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "Axis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Axis.html"
---

# Axis Property (ICircularPatternFeatureData)

Gets or sets the entity used to determine the direction of this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Axis As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Object

instance.Axis = value

value = instance.Axis
```

### C#

```csharp
System.object Axis {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Axis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Direction entity (see **Remarks**)

## VBA Syntax

See [CircularPatternFeatureData::Axis](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~Axis.html).

## Remarks

This property returns Nothing or null if you do not call [ICircularPatternFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICircularPatternFeatureData~AccessSelections.html) before using this property.

If [ICircularPatternFeatureData::GetAxisType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetAxisType.html) returns reference axis, use [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) to get [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html).

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::VarySketch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~VarySketch.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
