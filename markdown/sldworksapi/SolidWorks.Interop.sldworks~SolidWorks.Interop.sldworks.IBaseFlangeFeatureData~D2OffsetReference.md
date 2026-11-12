---
title: "D2OffsetReference Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "D2OffsetReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2OffsetReference.html"
---

# D2OffsetReference Property (IBaseFlangeFeatureData)

Obsolete. Superseded by [IBaseFlangeFeatureData::D2EndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2EndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property D2OffsetReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Object

instance.D2OffsetReference = value

value = instance.D2OffsetReference
```

### C#

```csharp
System.object D2OffsetReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D2OffsetReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the offset reference

## VBA Syntax

See [BaseFlangeFeatureData::D2OffsetReference](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~D2OffsetReference.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::D1OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1OffsetReference.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
