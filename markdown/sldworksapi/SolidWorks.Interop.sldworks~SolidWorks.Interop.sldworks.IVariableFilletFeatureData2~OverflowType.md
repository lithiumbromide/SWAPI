---
title: "OverflowType Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "OverflowType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~OverflowType.html"
---

# OverflowType Property (IVariableFilletFeatureData2)

Gets or sets the overflow type for this variable fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverflowType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Integer

instance.OverflowType = value

value = instance.OverflowType
```

### C#

```csharp
System.int OverflowType {get; set;}
```

### C++/CLI

```cpp
property System.int OverflowType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Overflow type as defined in [swFilletOverFlowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)

## VBA Syntax

See [VariableFilletFeatureData2::OverflowType](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~OverflowType.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
