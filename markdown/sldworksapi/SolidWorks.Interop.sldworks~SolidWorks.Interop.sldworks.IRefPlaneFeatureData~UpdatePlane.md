---
title: "UpdatePlane Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "UpdatePlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~UpdatePlane.html"
---

# UpdatePlane Property (IRefPlaneFeatureData)

Gets or sets whether to update this reference plane so that it is parallel to the screen.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpdatePlane As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean

instance.UpdatePlane = value

value = instance.UpdatePlane
```

### C#

```csharp
System.bool UpdatePlane {get; set;}
```

### C++/CLI

```cpp
property System.bool UpdatePlane {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to update the reference plane so that it is parallel to the screen, false to not

## VBA Syntax

See [RefPlaneFeatureData::UpdatePlane](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~UpdatePlane.html).

## Examples

[Update Plane (C#)](Update_Plane_Example_CSharp.htm)
[Update Plane (VB.NET)](Update_Plane_Example_VBNET.htm)
[Update Plane (VBA)](Update_Plane_Example_VB.htm)

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
