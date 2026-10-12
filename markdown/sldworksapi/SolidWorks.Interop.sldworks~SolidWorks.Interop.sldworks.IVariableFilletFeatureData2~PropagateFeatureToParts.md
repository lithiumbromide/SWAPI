---
title: "PropagateFeatureToParts Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "PropagateFeatureToParts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~PropagateFeatureToParts.html"
---

# PropagateFeatureToParts Property (IVariableFilletFeatureData2)

Gets or sets whether to extend the fillet feature to all affected parts in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateFeatureToParts As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Boolean

instance.PropagateFeatureToParts = value

value = instance.PropagateFeatureToParts
```

### C#

```csharp
System.bool PropagateFeatureToParts {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateFeatureToParts {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to extend fillet feature to all affected parts in the assembly, false to not

## VBA Syntax

See [VariableFilletFeatureData2::PropagateFeatureToParts](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~PropagateFeatureToParts.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
