---
title: "AlignWithEndFaces Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "AlignWithEndFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AlignWithEndFaces.html"
---

# AlignWithEndFaces Property (ISweepFeatureData)

Gets or sets whether to align this sweep with the end faces.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlignWithEndFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.AlignWithEndFaces = value

value = instance.AlignWithEndFaces
```

### C#

```csharp
System.bool AlignWithEndFaces {get; set;}
```

### C++/CLI

```cpp
property System.bool AlignWithEndFaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True aligns the sweep with the end faces (default for swept-cut and swept-boss), false does not (default for swept-surface) (see **Remarks**)

## VBA Syntax

See [SweepFeatureData::AlignWithEndFaces](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~AlignWithEndFaces.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

You must set this property to false if [ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.html) is set to [swTwistControlType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlConstantTwistAlongPath.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
