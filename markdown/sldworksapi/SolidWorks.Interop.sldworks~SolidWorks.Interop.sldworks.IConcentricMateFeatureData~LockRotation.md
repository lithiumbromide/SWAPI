---
title: "LockRotation Property (IConcentricMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConcentricMateFeatureData"
member: "LockRotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~LockRotation.html"
---

# LockRotation Property (IConcentricMateFeatureData)

Gets or sets whether to lock the rotation of the entities in this concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property LockRotation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConcentricMateFeatureData
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

True to lock rotation, false to not

## VBA Syntax

See [ConcentricMateFeatureData::LockRotation](ms-its:sldworksapivb6.chm::/sldworks~ConcentricMateFeatureData~LockRotation.html).

## Examples

See the [IConcentricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.html) example.

## See Also

[IConcentricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.html)
[IConcentricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
