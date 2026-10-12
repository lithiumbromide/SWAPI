---
title: "AngleReference Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "AngleReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AngleReference.html"
---

# AngleReference Property (IEdgeFlangeFeatureData)

Gets or sets the reference face used to define the bend angle of this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngleReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Object

instance.AngleReference = value

value = instance.AngleReference
```

### C#

```csharp
System.object AngleReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ AngleReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

## VBA Syntax

See [EdgeFlangeFeatureData::AngleReference](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~AngleReference.html).

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::PerpendicularToFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PerpendicularToFace.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
