---
title: "AutoSelect Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "AutoSelect"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~AutoSelect.html"
---

# AutoSelect Property (ICircularPatternFeatureData)

Gets whether to automatically select all bodies in a multibody part intersected by this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AutoSelect As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean

value = instance.AutoSelect
```

### C#

```csharp
System.bool AutoSelect {get;}
```

### C++/CLI

```cpp
property System.bool AutoSelect {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically select all bodies intersected by this circular pattern feature, false to specify affected bodies

## VBA Syntax

See [CircularPatternFeatureData::AutoSelect](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~AutoSelect.html).

## Remarks

This property is valid only if [ICircularPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GeometryPattern.html) is true.

Call [ICircularPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetFeatureScope.html) to set this property.

For more information, see the **Circular Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
