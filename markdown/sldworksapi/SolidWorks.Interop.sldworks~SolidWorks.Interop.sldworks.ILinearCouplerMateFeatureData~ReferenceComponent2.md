---
title: "ReferenceComponent2 Property (ILinearCouplerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: "ReferenceComponent2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~ReferenceComponent2.html"
---

# ReferenceComponent2 Property (ILinearCouplerMateFeatureData)

Gets or sets the reference component of the second mate entity of this linear/linear coupler mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferenceComponent2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Object

instance.ReferenceComponent2 = value

value = instance.ReferenceComponent2
```

### C#

```csharp
System.object ReferenceComponent2 {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferenceComponent2 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference component 2

## VBA Syntax

See [LinearCouplerMateFeatureData::ReferenceComponent12](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData~ReferenceComponent2.html).

## Remarks

Use this property to set up the motion of the second mated component with respect to a reference component. If you do not set this property, motion is with respect to the assembly origin.

## See Also

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
