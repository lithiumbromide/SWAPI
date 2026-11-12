---
title: "ClassificationType Property (IStraightElementData)"
project: "SOLIDWORKS API Help"
interface: "IStraightElementData"
member: "ClassificationType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData~ClassificationType.html"
---

# ClassificationType Property (IStraightElementData)

Gets or sets the classification type of this straight hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClassificationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStraightElementData
Dim value As System.Integer

instance.ClassificationType = value

value = instance.ClassificationType
```

### C#

```csharp
System.int ClassificationType {get; set;}
```

### C++/CLI

```cpp
property System.int ClassificationType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Classification type as defined in [swStraightHoleClassificationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightHoleClassificationType_e.html)

## VBA Syntax

See [StraightElementData::ClassificationType](ms-its:sldworksapivb6.chm::/sldworks~StraightElementData~ClassificationType.html).

## Remarks

This property is valid only if [IAdvancedHoleElementData::FastenerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~FastenerType.html) is set to [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html).swStandard*DowelHoles.

## See Also

[IStraightElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
[IStraightElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
