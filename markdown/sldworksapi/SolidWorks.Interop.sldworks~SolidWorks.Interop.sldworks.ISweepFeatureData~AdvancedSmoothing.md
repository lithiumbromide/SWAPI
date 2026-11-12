---
title: "AdvancedSmoothing Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "AdvancedSmoothing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AdvancedSmoothing.html"
---

# AdvancedSmoothing Property (ISweepFeatureData)

Gets or sets whether to apply advanced smoothing to this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AdvancedSmoothing As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.AdvancedSmoothing = value

value = instance.AdvancedSmoothing
```

### C#

```csharp
System.bool AdvancedSmoothing {get; set;}
```

### C++/CLI

```cpp
property System.bool AdvancedSmoothing {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables advanced smoothing, false (default) disables it

## VBA Syntax

See [SweepFeatureData::AdvancedSmoothing](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~AdvancedSmoothing.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
