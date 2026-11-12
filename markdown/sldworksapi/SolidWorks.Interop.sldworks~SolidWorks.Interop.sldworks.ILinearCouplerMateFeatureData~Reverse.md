---
title: "Reverse Property (ILinearCouplerMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearCouplerMateFeatureData"
member: "Reverse"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~Reverse.html"
---

# Reverse Property (ILinearCouplerMateFeatureData)

Gets or sets whether to reverse the direction of motion of the second mated component relative to the direction of motion of the first mated component of this linear/linear coupler mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reverse As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Boolean

instance.Reverse = value

value = instance.Reverse
```

### C#

```csharp
System.bool Reverse {get; set;}
```

### C++/CLI

```cpp
property System.bool Reverse {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of motion, false to not

## VBA Syntax

See [LinearCouplerMateFeatureData::Reverse](ms-its:sldworksapivb6.chm::/sldworks~LinearCouplerMateFeatureData~Reverse.html).

## Examples

See the [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html) examples.

## See Also

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
