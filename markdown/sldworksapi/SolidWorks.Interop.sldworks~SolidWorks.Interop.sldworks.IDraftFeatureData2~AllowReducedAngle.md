---
title: "AllowReducedAngle Property (IDraftFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData2"
member: "AllowReducedAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~AllowReducedAngle.html"
---

# AllowReducedAngle Property (IDraftFeatureData2)

Gets or sets the **Allow reduced angle** option for this draft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowReducedAngle As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData2
Dim value As System.Boolean

instance.AllowReducedAngle = value

value = instance.AllowReducedAngle
```

### C#

```csharp
System.bool AllowReducedAngle {get; set;}
```

### C++/CLI

```cpp
property System.bool AllowReducedAngle {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reduce the angle of the draft, false to not

## VBA Syntax

See [DraftFeatureData2::AllowReducedAngle](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData2~AllowReducedAngle.html).

## Remarks

See SOLIDWORKS Help for details about the **Allow reduced angle** setting.

## See Also

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.html)
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html)
[IDraftFeatureData2::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~Angle.html)
[IDraftFeatureData2::GetPartingLinesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetPartingLinesCount.html)
[IDraftFeatureData2::IGetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetPartingLines.html)
[IDraftFeatureData2::ISetPartingLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetPartingLines.html)
[IDraftFeatureData2::PartingLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~PartingLines.html)
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
