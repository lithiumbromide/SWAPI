---
title: "CenterOnBendLines Property (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "CenterOnBendLines"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~CenterOnBendLines.html"
---

# CenterOnBendLines Property (ISMCornerReliefData)

Gets and sets whether to center this corner relative to the bend lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property CenterOnBendLines As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim value As System.Boolean

instance.CenterOnBendLines = value

value = instance.CenterOnBendLines
```

### C#

```csharp
System.bool CenterOnBendLines {get; set;}
```

### C++/CLI

```cpp
property System.bool CenterOnBendLines {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to center relative to the bend lines, false to not

## VBA Syntax

See [SMCornerReliefData::CenterOnBendLines](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~CenterOnBendLines.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## Remarks

This property is valid only if:

- [ICornerReliefFeatureData::CornerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CornerType.html) is set to [swCornerReliefBendType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html).swCornerReliefBendType_TwoBend

- And -

- [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.html) is set to [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).:

  - swCornerCircularRelief
  - swCornerObroundRelief
  - swCornerRectangularRelief

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
