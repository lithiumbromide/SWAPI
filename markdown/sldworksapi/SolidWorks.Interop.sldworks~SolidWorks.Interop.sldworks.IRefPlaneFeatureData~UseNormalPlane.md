---
title: "UseNormalPlane Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "UseNormalPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UseNormalPlane.html"
---

# UseNormalPlane Property (IRefPlaneFeatureData)

Gets or sets whether to:

- Use the plane normal to the selected plane
- Automatically size the plane to either the geometry on which it is created or to the bounding box of the model geometry

## Syntax

### Visual Basic (Declaration)

```vb
Property UseNormalPlane As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean

instance.UseNormalPlane = value

value = instance.UseNormalPlane
```

### C#

```csharp
System.bool UseNormalPlane {get; set;}
```

### C++/CLI

```cpp
property System.bool UseNormalPlane {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a plane normal to the selected plane and automatically size the plane, false to not

## VBA Syntax

See [RefPlaneFeatureData::UseNormalPlane](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~UseNormalPlane.html).

## Remarks

If this property is true, then you can get or set [IRefPlaneFeatureData::Angle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Angle.html).

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::AutoSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~AutoSize.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
