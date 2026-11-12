---
title: "Type Property (ISurfRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfRevolveFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~Type.html"
---

# Type Property (ISurfRevolveFeatureData)

Gets or sets the type for this surface revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfRevolveFeatureData
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Revolution type as defined in [swRevolveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRevolveType_e.html)

## VBA Syntax

See [SurfRevolveFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~SurfRevolveFeatureData~Type.html).

## Examples

See [ISurfRevolveFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfRevolveFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.html)
[ISurfRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
