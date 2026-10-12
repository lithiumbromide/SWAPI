---
title: "SynchronizeFlexibleComponents Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "SynchronizeFlexibleComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SynchronizeFlexibleComponents.html"
---

# SynchronizeFlexibleComponents Property (ILocalLinearPatternFeatureData)

Gets or sets whether to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components in this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SynchronizeFlexibleComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean

instance.SynchronizeFlexibleComponents = value

value = instance.SynchronizeFlexibleComponents
```

### C#

```csharp
System.bool SynchronizeFlexibleComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool SynchronizeFlexibleComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components, false to not

## VBA Syntax

See [LocalLinearPatternFeatureData::SynchronizeFlexibleComponents](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~SynchronizeFlexibleComponents.html).

## Examples

See the [ILocalLinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html) example.

## Remarks

This property is valid for a linear pattern of flexible subassemblies.

If this property is set to true, then when you move components in the seed flexible subassembly, components in the patterned flexible subassemblies also move, and vice versa.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
