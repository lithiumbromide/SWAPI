---
title: "MateEntity2 Property (ILinearCouplerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: "MateEntity2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~MateEntity2.html"
---

# MateEntity2 Property (ILinearCouplerMateFeatureData)

Gets or sets the entity of the second mated component of this linear/linear coupler mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property MateEntity2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Object

instance.MateEntity2 = value

value = instance.MateEntity2
```

### C#

```csharp
System.object MateEntity2 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MateEntity2 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Second mated component entity

## VBA Syntax

See [LinearCouplerMateFeatureData::MateEntity2](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData~MateEntity2.html).

## Examples

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html) examples.

## See Also

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
