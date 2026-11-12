---
title: "UsePositionTrimSideBends Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "UsePositionTrimSideBends"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionTrimSideBends.html"
---

# UsePositionTrimSideBends Property (IEdgeFlangeFeatureData)

Gets or sets whether to trim side bends for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property UsePositionTrimSideBends As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean

instance.UsePositionTrimSideBends = value

value = instance.UsePositionTrimSideBends
```

### C#

```csharp
System.bool UsePositionTrimSideBends {get; set;}
```

### C++/CLI

```cpp
property System.bool UsePositionTrimSideBends {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True trims side bends, false does not (default)

## VBA Syntax

See [EdgeFlangeFeatureData::UsePositionTrimSideBends](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~UsePositionTrimSideBends.html).

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::GetPositionReferenceType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetPositionReferenceType.html)
[IEdgeFlangeFeatureData::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionType.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
