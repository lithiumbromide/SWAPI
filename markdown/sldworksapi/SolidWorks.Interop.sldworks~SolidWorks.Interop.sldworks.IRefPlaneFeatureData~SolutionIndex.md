---
title: "SolutionIndex Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "SolutionIndex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~SolutionIndex.html"
---

# SolutionIndex Property (IRefPlaneFeatureData)

Gets or sets the intended plane when there are multiple planes from which to select for an on-surface reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolutionIndex As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim value As System.Integer

instance.SolutionIndex = value

value = instance.SolutionIndex
```

### C#

```csharp
System.int SolutionIndex {get; set;}
```

### C++/CLI

```cpp
property System.int SolutionIndex {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value indicating intended plane (0-based index)

## VBA Syntax

See [RefPlaneFeatureData::SolutionIndex](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~SolutionIndex.html).

## Remarks

This property corresponds to the **Other Solutions** check box that appears on the Plane PropertyManager page when there is more than one plane from which to select when creating an on-surface reference plane in SOLIDWORKS.

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
