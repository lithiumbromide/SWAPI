---
title: "D1OffsetReference Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "D1OffsetReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1OffsetReference.html"
---

# D1OffsetReference Property (IBaseFlangeFeatureData)

Obsolete. Superseded by [IBaseFlangeFeatureData::D1EndConditionReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1EndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property D1OffsetReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Object

instance.D1OffsetReference = value

value = instance.D1OffsetReference
```

### C#

```csharp
System.object D1OffsetReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D1OffsetReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the offset reference

## VBA Syntax

See [BaseFlangeFeatureData::D1OffsetReference](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~D1OffsetReference.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::D2OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D2OffsetReference.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
