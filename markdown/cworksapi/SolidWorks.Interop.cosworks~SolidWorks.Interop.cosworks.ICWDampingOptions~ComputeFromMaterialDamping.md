---
title: "ComputeFromMaterialDamping Property (ICWDampingOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDampingOptions"
member: "ComputeFromMaterialDamping"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~ComputeFromMaterialDamping.html"
---

# ComputeFromMaterialDamping Property (ICWDampingOptions)

Obsolete. Superseded by [ICWDampingOptions::ComputeFromMaterialDamping2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~ComputeFromMaterialDamping2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ComputeFromMaterialDamping As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDampingOptions
Dim value As System.Integer

instance.ComputeFromMaterialDamping = value

value = instance.ComputeFromMaterialDamping
```

### C#

```csharp
System.int ComputeFromMaterialDamping {get; set;}
```

### C++/CLI

```cpp
property System.int ComputeFromMaterialDamping {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 to not use the material damping ratio; 1 to use the material damping ratio (see **Remarks**)

## VBA Syntax

See [CWDampingOptions::ComputeFromMaterialDamping](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDampingOptions~ComputeFromMaterialDamping.html).

## Remarks

For more information about modal damping, see the SOLIDWORKS Simulation Help.

## See Also

[ICWDampingOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html)
[ICWDampingOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions_members.html)
[ICWDampingOptions::GetDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~GetDampingRatios.html)
[ICWDampingOptions::SetDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~SetDampingRatios.html)
[ICWDampingOptions::DampingType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~DampingType.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
