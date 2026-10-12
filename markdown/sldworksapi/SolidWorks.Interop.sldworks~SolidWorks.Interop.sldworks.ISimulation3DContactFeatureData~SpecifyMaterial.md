---
title: "SpecifyMaterial Property (ISimulation3DContactFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulation3DContactFeatureData"
member: "SpecifyMaterial"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~SpecifyMaterial.html"
---

# SpecifyMaterial Property (ISimulation3DContactFeatureData)

Gets or sets whether to use materials in a 3D Contact feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpecifyMaterial As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulation3DContactFeatureData
Dim value As System.Boolean

instance.SpecifyMaterial = value

value = instance.SpecifyMaterial
```

### C#

```csharp
System.bool SpecifyMaterial {get; set;}
```

### C++/CLI

```cpp
property System.bool SpecifyMaterial {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use materials, false to not

## VBA Syntax

See [Simulation3DContactFeatureData::SpecifyMaterial](ms-its:sldworksapivb6.chm::/sldworks~Simulation3DContactFeatureData~SpecifyMaterial.html).

## Examples

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html) examples.

## Remarks

Set to false to modify elastic properties:

- [ISimulation3DContactFeatureData::Stiffness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Stiffness.html)
- [ISimulation3DContactFeatureData::Exponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Exponent.html)
- [ISimulation3DContactFeatureData::MaxDamping](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaxDamping.html)
- [ISimulation3DContactFeatureData::Penetration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Penetration.html)

## See Also

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.html)
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html)
[ISimulation3DContactFeatureData::MaterialID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaterialID.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
