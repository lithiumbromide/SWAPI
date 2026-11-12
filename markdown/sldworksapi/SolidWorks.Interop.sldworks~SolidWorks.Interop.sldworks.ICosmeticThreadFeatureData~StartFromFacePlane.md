---
title: "StartFromFacePlane Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "StartFromFacePlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~StartFromFacePlane.html"
---

# StartFromFacePlane Property (ICosmeticThreadFeatureData)

Gets or sets the start face or plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartFromFacePlane As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Object

instance.StartFromFacePlane = value

value = instance.StartFromFacePlane
```

### C#

```csharp
System.object StartFromFacePlane {get; set;}
```

### C++/CLI

```cpp
property System.Object^ StartFromFacePlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [IRefPlane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [CosmeticThreadFeatureData::StartFromFacePlane](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~StartFromFacePlane.html).

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
