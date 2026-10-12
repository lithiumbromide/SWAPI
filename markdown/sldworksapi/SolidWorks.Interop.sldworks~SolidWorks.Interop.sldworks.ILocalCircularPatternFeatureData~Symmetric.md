---
title: "Symmetric Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "Symmetric"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Symmetric.html"
---

# Symmetric Property (ILocalCircularPatternFeatureData)

Gets or sets whether Direction 2 properties are symmetric with those of Direction 1 of this bidirectional circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Symmetric As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Boolean

instance.Symmetric = value

value = instance.Symmetric
```

### C#

```csharp
System.bool Symmetric {get; set;}
```

### C++/CLI

```cpp
property System.bool Symmetric {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if Direction 2 properties mirror Direction 1 properties, false if not

## VBA Syntax

See [LocalCircularPatternFeatureData::Symmetric](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~Symmetric.html).

## Remarks

This property is only available when [ILocalCircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Direction2.html) is true.

If this property is set to false, then you must specify:

- [ILocalCircularPatternFeatureData::EqualSpacing2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.html)
- [ILocalCircularPatternFeatureData::TotalInstances2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances2.html)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
