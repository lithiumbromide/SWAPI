---
title: "SimplifyGeometry Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "SimplifyGeometry"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~SimplifyGeometry.html"
---

# SimplifyGeometry Property (IOneBendFeatureData)

Gets or sets whether to simplify the geometry for this bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SimplifyGeometry As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Boolean

instance.SimplifyGeometry = value

value = instance.SimplifyGeometry
```

### C#

```csharp
System.bool SimplifyGeometry {get; set;}
```

### C++/CLI

```cpp
property System.bool SimplifyGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to simplify the geometry, false to not

## VBA Syntax

See [OneBendFeatureData::SimplifyGeometry](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~SimplifyGeometry.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
