---
title: "OffsetReference Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "OffsetReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetReference.html"
---

# OffsetReference Property (IJogFeatureData)

Gets or sets the offset reference for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Object

instance.OffsetReference = value

value = instance.OffsetReference
```

### C#

```csharp
System.object OffsetReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ OffsetReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset reference

## VBA Syntax

See [JogFeatureData::OffsetReference](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~OffsetReference.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)
[IJogFeatureData::GetOffsetReferenceType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~GetOffsetReferenceType.html)
[IJogFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetDistance.html)
[IJogFeatureData::OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~OffsetType.html)
[IJogFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
