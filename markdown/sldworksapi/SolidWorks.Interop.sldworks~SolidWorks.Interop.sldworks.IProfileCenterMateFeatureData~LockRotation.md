---
title: "LockRotation Property (IProfileCenterMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProfileCenterMateFeatureData"
member: "LockRotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData~LockRotation.html"
---

# LockRotation Property (IProfileCenterMateFeatureData)

Gets or sets whether to lock the rotation of this profile center mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property LockRotation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileCenterMateFeatureData
Dim value As System.Boolean

instance.LockRotation = value

value = instance.LockRotation
```

### C#

```csharp
System.bool LockRotation {get; set;}
```

### C++/CLI

```cpp
property System.bool LockRotation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to lock the rotation, false to not

## VBA Syntax

See [ProfileCenterMateFeatureData::LockRotation](ms-its:sldworksapivb6.chm::/sldworks~ProfileCenterMateFeatureData~LockRotation.html).

## Examples

See the [IProfileCenterMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html) examples.

## See Also

[IProfileCenterMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html)
[IProfileCenterMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
