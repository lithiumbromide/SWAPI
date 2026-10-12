---
title: "Bidirectional Property (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "Bidirectional"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Bidirectional.html"
---

# Bidirectional Property (IProjectionCurveFeatureData)

Gets or sets whether the sketch is projected bidirectionally.

## Syntax

### Visual Basic (Declaration)

```vb
Property Bidirectional As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData
Dim value As System.Boolean

instance.Bidirectional = value

value = instance.Bidirectional
```

### C#

```csharp
System.bool Bidirectional {get; set;}
```

### C++/CLI

```cpp
property System.bool Bidirectional {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if bidirectional, false if not

## VBA Syntax

See [ProjectionCurveFeatureData::Bidirectional](ms-its:sldworksapivb6.chm::/sldworks~ProjectionCurveFeatureData~Bidirectional.html).

## Examples

See the [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html) example.

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
