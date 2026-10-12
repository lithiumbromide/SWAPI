---
title: "GeometryPattern Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "GeometryPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GeometryPattern.html"
---

# GeometryPattern Property (ICircularPatternFeatureData)

Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeometryPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean

instance.GeometryPattern = value

value = instance.GeometryPattern
```

### C#

```csharp
System.bool GeometryPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool GeometryPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use only the geometry of the feature to create the pattern (faster), false to pattern and solve each instance of the feature in its entirety (slower)

## VBA Syntax

See [CircularPatternFeatureData::GeometryPattern](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~GeometryPattern.html).

## Remarks

This property is valid only if [ICircularPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~BodyPattern.html) is false.

If this property is set to true, you can call [ICircularPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SetFeatureScope.html).

For more information, see the **Circular Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
