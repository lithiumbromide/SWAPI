---
title: "Centerline Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "Centerline"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~Centerline.html"
---

# Centerline Property (ILoftFeatureData)

Gets and sets the centerline for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Centerline As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Object

instance.Centerline = value

value = instance.Centerline
```

### C#

```csharp
System.object Centerline {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Centerline {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[ICenterLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine.html)

## VBA Syntax

See [LoftFeatureData::CenterLine](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~CenterLine.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
