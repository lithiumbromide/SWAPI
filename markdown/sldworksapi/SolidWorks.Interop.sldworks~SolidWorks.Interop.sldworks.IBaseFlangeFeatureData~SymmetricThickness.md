---
title: "SymmetricThickness Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "SymmetricThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~SymmetricThickness.html"
---

# SymmetricThickness Property (IBaseFlangeFeatureData)

Gets or sets whether to symmetrically thicken this bi-directional base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SymmetricThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.SymmetricThickness = value

value = instance.SymmetricThickness
```

### C#

```csharp
System.bool SymmetricThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool SymmetricThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to thicken symmetrically, false to not

## VBA Syntax

See [BaseFlangeFeatureData::SymmetricThickness](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~SymmetricThickness.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
