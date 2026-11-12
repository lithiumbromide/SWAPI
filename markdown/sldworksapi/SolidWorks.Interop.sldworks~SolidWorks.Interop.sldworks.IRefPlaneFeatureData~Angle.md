---
title: "Angle Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Angle.html"
---

# Angle Property (IRefPlaneFeatureData)

Gets or sets the angle of the reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians

## VBA Syntax

See [RefPlaneFeatureData::Angle](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~Angle.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::UseNormalPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UseNormalPlane.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
