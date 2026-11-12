---
title: "MateEntity1 Property (ILinearCouplerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: "MateEntity1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~MateEntity1.html"
---

# MateEntity1 Property (ILinearCouplerMateFeatureData)

Gets or sets the entity of the first mated component of this linear/linear coupler mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateEntity1 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Object

instance.MateEntity1 = value

value = instance.MateEntity1
```

### C#

```csharp
System.object MateEntity1 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MateEntity1 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

First mated component entity ([face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html))

## VBA Syntax

See [LinearCouplerMateFeatureData::MateEntity1](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData~MateEntity1.html).

## Examples

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html) examples.

## See Also

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
