---
title: "BodiesToBeTrimmed Property (IWeldmentTrimExtendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentTrimExtendFeatureData"
member: "BodiesToBeTrimmed"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html"
---

# BodiesToBeTrimmed Property (IWeldmentTrimExtendFeatureData)

Gets or sets the bodies to trim.

## Syntax

### Visual Basic (Declaration)

```vb
Property BodiesToBeTrimmed As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentTrimExtendFeatureData
Dim value As System.Object

instance.BodiesToBeTrimmed = value

value = instance.BodiesToBeTrimmed
```

### C#

```csharp
System.object BodiesToBeTrimmed {get; set;}
```

### C++/CLI

```cpp
property System.Object^ BodiesToBeTrimmed {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to trim (see Remarks)

## VBA Syntax

See [WeldmentTrimExtendFeatureData::BodiesToBeTrimmed](ms-its:sldworksapivb6.chm::/sldworks~WeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html).

## Remarks

Only end-trim corner types (swEndConditionTrim) can have multiple bodies to trim. Use [IWeldmentTrimExtendFeatureData::CornerType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~CornerType.html) to determine the type of corner.

You must set the bodies to trim and set the [trimming boundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentTrimExtendFeatureData~SetTrimmingBoundary.html) if changing a corner type.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentTrimExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData.html)
[IWeldmentTrimExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html)
[IWeldmentTrimExtendFeatureData::GetBodiesToBeTrimmedCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~GetBodiesToBeTrimmedCount.html)
[IWeldmentTrimExtendFeatureData::IGetBodiesToBeTrimmed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~IGetBodiesToBeTrimmed.html)
[IWeldmentTrimExtendFeatureData::ISetBodiesToBeTrimmed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~ISetBodiesToBeTrimmed.html)
[IWeldmentTrimExtendFeatureData::BodiesToBeTrimmed Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData~BodiesToBeTrimmed.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
