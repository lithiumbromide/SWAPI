---
title: "HasTreatInterferenceAsShrinkFit Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "HasTreatInterferenceAsShrinkFit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasTreatInterferenceAsShrinkFit.html"
---

# HasTreatInterferenceAsShrinkFit Property (IMate2)

Gets whether interference in this mate is treated as shrink/press fit.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasTreatInterferenceAsShrinkFit As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

value = instance.HasTreatInterferenceAsShrinkFit
```

### C#

```csharp
System.bool HasTreatInterferenceAsShrinkFit {get;}
```

### C++/CLI

```cpp
property System.bool HasTreatInterferenceAsShrinkFit {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if interference is treated as shrink/press fit, false if not

## VBA Syntax

See [Mate2::HasTreatInterferenceAsShrinkFit](ms-its:sldworksapivb6.chm::/sldworks~Mate2~HasTreatInterferenceAsShrinkFit.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
