---
title: "ComputeFromMaterialDamping2 Property (ICWDampingOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDampingOptions"
member: "ComputeFromMaterialDamping2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~ComputeFromMaterialDamping2.html"
---

# ComputeFromMaterialDamping2 Property (ICWDampingOptions)

Gets and sets whether to use the material damping ratio to calculate modal damping ratios.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComputeFromMaterialDamping2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDampingOptions
Dim value As System.Boolean

instance.ComputeFromMaterialDamping2 = value

value = instance.ComputeFromMaterialDamping2
```

### C#

```csharp
System.bool ComputeFromMaterialDamping2 {get; set;}
```

### C++/CLI

```cpp
property System.bool ComputeFromMaterialDamping2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

0 or false to not use the material damping ratio; -1 or true to use the material damping ratio (see **Remarks**)

## Examples

See the [ICWDampingOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

For more information about modal damping, see the SOLIDWORKS Simulation Help.

## See Also

[ICWDampingOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html)
[ICWDampingOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
