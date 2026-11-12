---
title: "PerpendicularToFace Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "PerpendicularToFace"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PerpendicularToFace.html"
---

# PerpendicularToFace Property (IEdgeFlangeFeatureData)

Gets or sets whether to set this edge flange perpendicular to the angle reference face.

## Syntax

### Visual Basic (Declaration)

```vb
Property PerpendicularToFace As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean

instance.PerpendicularToFace = value

value = instance.PerpendicularToFace
```

### C#

```csharp
System.bool PerpendicularToFace {get; set;}
```

### C++/CLI

```cpp
property System.bool PerpendicularToFace {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to set this edge flange perpendicular to the angle reference face, false to set it parallel to the angle reference face (default)

## VBA Syntax

See [EdgeFlangeFeatureData::PerpendicularToFace](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~PerpendicularToFace.html).

## Remarks

This property is valid only if [IEdgeFlangeFeatureData::AngleReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AngleReference.html) is not null.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
