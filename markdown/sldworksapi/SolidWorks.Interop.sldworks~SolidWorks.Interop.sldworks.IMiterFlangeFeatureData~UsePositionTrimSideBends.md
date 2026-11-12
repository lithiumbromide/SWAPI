---
title: "UsePositionTrimSideBends Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "UsePositionTrimSideBends"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~UsePositionTrimSideBends.html"
---

# UsePositionTrimSideBends Property (IMiterFlangeFeatureData)

Gets or sets whether to remove extra material in neighboring bends for this miter flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UsePositionTrimSideBends As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
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

True to remove extra material in neighboring bends, false to not remove material

## VBA Syntax

See [MiterFlangeFeatureData::UsePositionTrimSideBends](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~UsePositionTrimSideBends.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
