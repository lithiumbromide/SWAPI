---
title: "ReferenceComponent1 Property (ILinearCouplerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: "ReferenceComponent1"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~ReferenceComponent1.html"
---

# ReferenceComponent1 Property (ILinearCouplerMateFeatureData)

Gets or sets the reference component of the first mate entity of this linear coupler mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferenceComponent1 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Object

instance.ReferenceComponent1 = value

value = instance.ReferenceComponent1
```

### C#

```csharp
System.object ReferenceComponent1 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferenceComponent1 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference component 1

## VBA Syntax

See [LinearCouplerMateFeatureData::ReferenceComponent1](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData~ReferenceComponent1.html).

## Remarks

Use this property to set up the motion of the first mated component with respect to a reference component. If you do not set this property, motion is with respect to the assembly origin.

## See Also

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
