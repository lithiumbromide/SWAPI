---
title: "AutoSize Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "AutoSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~AutoSize.html"
---

# AutoSize Property (IRefPlaneFeatureData)

Gets or sets whether to automatically size the reference plane feature to either the geometry on which it is created or to the bounding box of the model geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSize As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean

instance.AutoSize = value

value = instance.AutoSize
```

### C#

```csharp
System.bool AutoSize {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSize {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically size the reference plane, false to not

## VBA Syntax

See [RefPlaneFeatureData::AutoSize](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~AutoSize.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::UseNormalPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UseNormalPlane.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
