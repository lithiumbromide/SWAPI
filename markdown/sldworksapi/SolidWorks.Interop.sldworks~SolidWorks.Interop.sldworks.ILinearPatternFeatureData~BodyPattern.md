---
title: "BodyPattern Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "BodyPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html"
---

# BodyPattern Property (ILinearPatternFeatureData)

Gets or sets whether to base this linear pattern feature on bodies and structure systems or features and faces.

## Syntax

### Visual Basic (Declaration)

```vb
Property BodyPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean

instance.BodyPattern = value

value = instance.BodyPattern
```

### C#

```csharp
System.bool BodyPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool BodyPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for bodies and structure systems, false for features and faces

## VBA Syntax

See [LinearPatternFeatureData::BodyPattern](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~BodyPattern.html).

## Examples

[Change Linear Pattern (C#)](Change_Linear_Pattern_Example_CSharp.htm)
[Change Linear Pattern (VB.NET)](Change_Linear_Pattern_Example_VBNET.htm)
[Change Linear Pattern (VBA)](Change_Linear_Pattern_Example_VB.htm)

## Remarks

If this property is:

- True, use [ILinearPatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternBodyArray.html) to specify the bodies to pattern and [ILinearPatternFeatureData::StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~StructureSystemToPatternArray.html) to specify the structure systems to pattern.
- False, use [ILinearPatternFeatureData::PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFaceArray.html) or [ILinearPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFeatureArray.html) to specify the face or feature to pattern.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::PatternElement Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternElement.html)
[ILinearPatternFeatureData::IGetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternBodyArray.html)
[ILinearPatternFeatureData::IGetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternFaceArray.html)
[ILinearPatternFeatureData::IGetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternFeatureArray.html)
[ILinearPatternFeatureData::ISetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternBodyArray.html)
[ILinearPatternFeatureData::ISetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternFaceArray.html)
[ILinearPatternFeatureData::ISetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternFeatureArray.html)

## Availability

SOLIDWORKS 2015 SP4, Revision Number 23.4
