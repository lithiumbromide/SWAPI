---
title: "ReferencePoint Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "ReferencePoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint.html"
---

# ReferencePoint Property (ISketchPatternFeatureData)

Gets or sets the reference point for this sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Object

instance.ReferencePoint = value

value = instance.ReferencePoint
```

### C#

```csharp
System.object ReferencePoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferencePoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference point for this sketch pattern feature

## VBA Syntax

See [SketchPatternFeatureData::ReferencePoint](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~ReferencePoint.html).

## Remarks

This property is valid only if [ISketchPatternFeatureData::GetReferencePointType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetReferencePointType.html) does not return -1.

Before calling this property, call [ISketchPatternFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPatternFeatureData~AccessSelections.html) or [ISketchPatternFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPatternFeatureData~IAccessSelections2.html) to access the reference point.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
