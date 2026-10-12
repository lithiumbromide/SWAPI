---
title: "Type2 Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "Type2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type2.html"
---

# Type2 Property (IRefPlaneFeatureData)

Gets whether the reference plane is constraint based; thus, created in SOLIDWORKS 2010 and later.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Integer

instance.Type2 = value

value = instance.Type2
```

### C#

```csharp
System.int Type2 {get; set;}
```

### C++/CLI

```cpp
property System.int Type2 {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of reference plane as defined in [swRefPlaneType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneType_e.html) (see **Remarks**)

## VBA Syntax

See [RefPlaneFeatureData::Type2](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~Type2.html).

## Examples

[Insert Reference Plane (C#)](Insert_Reference_Plane_Example_CSharp.htm)
[Insert Reference Plane (VB.NET)](Insert_Reference_Plane_Example_VBNET.htm)
[Insert Reference Plane (VBA)](Insert_Reference_Plane_Example_VB.htm)

## Remarks

If IRefPlaneFeatureData::Type2 returns swRefPlaneConstraintBase, then the reference plane is constraint based and was created in SOLIDWORKS 2010 or later. To determine if a constraint-based reference plane has angle or offset distances references, call [IRefPlaneFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Type.html):

- swRefPlaneAngle is returned for angle references.
- swRefPlaneDistance is returned for offset distance references.

Otherwise, the reference plane is not constraint based and was created in SOLIDWORKS 2009 or earlier. Call [IRefPlaneFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Type.html) to determine its type.

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
