---
title: "ProjectionType Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "ProjectionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ProjectionType.html"
---

# ProjectionType Property (IRefPlaneFeatureData)

Gets or sets the projection type for this on-surface reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProjectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Integer

instance.ProjectionType = value

value = instance.ProjectionType
```

### C#

```csharp
System.int ProjectionType {get; set;}
```

### C++/CLI

```cpp
property System.int ProjectionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of a plane on a surface as defined in [swOnSurfacePlaneProjectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOnSurfacePlaneProjectType_e.html)

## VBA Syntax

See [RefPlaneFeatureData::ProjectionType](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~ProjectionType.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
