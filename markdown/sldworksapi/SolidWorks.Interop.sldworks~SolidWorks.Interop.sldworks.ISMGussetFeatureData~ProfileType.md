---
title: "ProfileType Property (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ProfileType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileType.html"
---

# ProfileType Property (ISMGussetFeatureData)

Gets or sets the type of profile of this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData
Dim value As System.Integer

instance.ProfileType = value

value = instance.ProfileType
```

### C#

```csharp
System.int ProfileType {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of profile as defined in [swSheetMetalGussetProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalGussetProfileType_e.html)

## VBA Syntax

See [SMGussetFeatureData::ProfileType](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ProfileType.html).

## Remarks

This property is valid only when editing an existing sheet metal gusset.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
