---
title: "ReverseDirection Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (IRefPlaneFeatureData)

Obsolete. Superseded by [IRefPlaneFeatureData::ReversedReferenceDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReversedReferenceDirection.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction, false to not

## VBA Syntax

See [RefPlaneFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~ReverseDirection.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
