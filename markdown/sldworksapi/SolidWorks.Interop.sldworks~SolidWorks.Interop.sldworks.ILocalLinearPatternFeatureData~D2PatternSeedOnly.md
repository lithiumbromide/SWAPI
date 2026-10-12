---
title: "D2PatternSeedOnly Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D2PatternSeedOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2PatternSeedOnly.html"
---

# D2PatternSeedOnly Property (ILocalLinearPatternFeatureData)

Gets or sets whether to create a pattern in Direction 2 using the seed component only, without replicating the pattern instances of Direction 1, in this bidirectional linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2PatternSeedOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean

instance.D2PatternSeedOnly = value

value = instance.D2PatternSeedOnly
```

### C#

```csharp
System.bool D2PatternSeedOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool D2PatternSeedOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create a pattern in Direction 2 using the seed component only without replicating the pattern instances of Direction 1, false to not

## VBA Syntax

See [LocalLinearPatternFeatureData::D2PatternSeedOnly](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D2PatternSeedOnly.html).

## Examples

See the [ILocalLinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html) example.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
