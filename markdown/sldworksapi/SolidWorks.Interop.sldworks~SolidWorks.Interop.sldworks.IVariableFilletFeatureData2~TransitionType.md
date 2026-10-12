---
title: "TransitionType Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "TransitionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~TransitionType.html"
---

# TransitionType Property (IVariableFilletFeatureData2)

Gets or sets the type of transition between this variable fillet and an adjacent fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransitionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Integer

instance.TransitionType = value

value = instance.TransitionType
```

### C#

```csharp
System.int TransitionType {get; set;}
```

### C++/CLI

```cpp
property System.int TransitionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of transition as defined in [swVariableRadiusFilletOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVariableRadiusFilletOptions_e.html)

## VBA Syntax

See [VariableFilletFeatureData2::TransitionType](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~TransitionType.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
