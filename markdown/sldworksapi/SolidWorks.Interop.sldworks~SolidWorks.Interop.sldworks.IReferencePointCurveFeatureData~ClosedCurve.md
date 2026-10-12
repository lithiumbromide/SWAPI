---
title: "ClosedCurve Property (IReferencePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReferencePointCurveFeatureData"
member: "ClosedCurve"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ClosedCurve.html"
---

# ClosedCurve Property (IReferencePointCurveFeatureData)

Gets or sets whether the curve is closed or not.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClosedCurve As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IReferencePointCurveFeatureData
Dim value As System.Boolean

instance.ClosedCurve = value

value = instance.ClosedCurve
```

### C#

```csharp
System.bool ClosedCurve {get; set;}
```

### C++/CLI

```cpp
property System.bool ClosedCurve {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if curve is closed, false if not

## VBA Syntax

See [ReferencePointCurveFeatureData::ClosedCurve](ms-its:sldworksapivb6.chm::/sldworks~ReferencePointCurveFeatureData~ClosedCurve.html).

## Examples

See the [IReferencePointCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html) examples.

## See Also

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html)
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
