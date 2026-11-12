---
title: "IsCut Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "IsCut"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.html"
---

# IsCut Property (IIndentFeatureData)

Gets or sets whether to remove the intersection area of the [target body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IsCut As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Boolean

instance.IsCut = value

value = instance.IsCut
```

### C#

```csharp
System.bool IsCut {get; set;}
```

### C++/CLI

```cpp
property System.bool IsCut {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to remove the intersection area of the target body, false to not

## VBA Syntax

See [IndentFeatureData::IsCut](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~IsCut.html).

## Remarks

If this property is set to true, then there is no [thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Thickness.html), but [clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance.html) is applied.

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
