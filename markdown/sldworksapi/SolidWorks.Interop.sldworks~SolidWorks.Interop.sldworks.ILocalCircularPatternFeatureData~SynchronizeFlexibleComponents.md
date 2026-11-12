---
title: "SynchronizeFlexibleComponents Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "SynchronizeFlexibleComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SynchronizeFlexibleComponents.html"
---

# SynchronizeFlexibleComponents Property (ILocalCircularPatternFeatureData)

Gets or sets whether to synchronize the movement of flexible subassembly components in this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SynchronizeFlexibleComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
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

True to synchronize the movement of flexible subassembly components, false to not

## VBA Syntax

See [LocalCircularPatternFeatureData::SynchronizeFlexibleComponents](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~SynchronizeFlexibleComponents.html).

## Remarks

If this property is set to true, then when you move components in the seed flexible subassembly, components in the patterned instances move, and vice versa.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
