---
title: "ReverseDirection Property (ISurfRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfRevolveFeatureData"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~ReverseDirection.html"
---

# ReverseDirection Property (ISurfRevolveFeatureData)

Gets or sets the reverse direction setting for this surface revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfRevolveFeatureData
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True enables the reverse direction setting, false disables it

## VBA Syntax

See [SurfRevolveFeatureData::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~SurfRevolveFeatureData~ReverseDirection.html).

## Examples

See [ISurfRevolveFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfRevolveFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.html)
[ISurfRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
