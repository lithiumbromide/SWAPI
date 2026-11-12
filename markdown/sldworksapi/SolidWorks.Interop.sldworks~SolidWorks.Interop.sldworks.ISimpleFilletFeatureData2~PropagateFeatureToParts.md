---
title: "PropagateFeatureToParts Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "PropagateFeatureToParts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~PropagateFeatureToParts.html"
---

# PropagateFeatureToParts Property (ISimpleFilletFeatureData2)

Gets or sets whether to extend the assembly simple fillet feature to all affected parts.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateFeatureToParts As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
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

True to extend the assembly simple fillet feature to all affected parts, false to not

## VBA Syntax

See [SimpleFilletFeatureData2::PropagateFeatureToParts](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~PropagateFeatureToParts.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelect.html)
[ISimpleFilletFeatureData2::AutoSelectComponents Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AutoSelectComponents.html)
[ISimpleFilletFeatureData2::AssemblyFeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AssemblyFeatureScope.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
