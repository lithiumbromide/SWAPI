---
title: "MainBody Property (ICombineBodiesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICombineBodiesFeatureData"
member: "MainBody"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData~MainBody.html"
---

# MainBody Property (ICombineBodiesFeatureData)

Gets or sets the main body to keep when subtracting bodies from this combine feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MainBody As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ICombineBodiesFeatureData
Dim value As Body2

instance.MainBody = value

value = instance.MainBody
```

### C#

```csharp
Body2 MainBody {get; set;}
```

### C++/CLI

```cpp
property Body2^ MainBody {
   Body2^ get();
   void set (    Body2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of main body to keep

## VBA Syntax

See [CombineBodiesFeatureData::MainBody](ms-its:sldworksapivb6.chm::/sldworks~CombineBodiesFeatureData~MainBody.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICombineBodiesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData.html)
[ICombineBodiesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
