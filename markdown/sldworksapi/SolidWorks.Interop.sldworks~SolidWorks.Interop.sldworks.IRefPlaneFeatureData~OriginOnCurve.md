---
title: "OriginOnCurve Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "OriginOnCurve"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~OriginOnCurve.html"
---

# OriginOnCurve Property (IRefPlaneFeatureData)

Gets or sets whether to place the origin on the curve for this reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OriginOnCurve As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean

instance.OriginOnCurve = value

value = instance.OriginOnCurve
```

### C#

```csharp
System.bool OriginOnCurve {get; set;}
```

### C++/CLI

```cpp
property System.bool OriginOnCurve {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to place the origin on the curve, false to place the origin on the vertex or point

## VBA Syntax

See [RefPlaneFeatureData::OriginOnCurve](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~OriginOnCurve.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
