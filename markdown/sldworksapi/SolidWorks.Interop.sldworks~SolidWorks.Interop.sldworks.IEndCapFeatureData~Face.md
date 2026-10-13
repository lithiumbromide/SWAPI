---
title: "Face Property (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "Face"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~Face.html"
---

# Face Property (IEndCapFeatureData)

Gets the face that is capped or sets the face to cap.

## Syntax

### Visual Basic (Declaration)

```vb
Property Face As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData
Dim value As Face2

instance.Face = value

value = instance.Face
```

### C#

```csharp
Face2 Face {get; set;}
```

### C++/CLI

```cpp
property Face2^ Face {
   Face2^ get();
   void set (    Face2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) object

## VBA Syntax

See [EndCapFeatureData::Face](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~Face.html).

## Examples

[List End-cap Feature Properties (VBA)](List_End-Cap_Feature_Properties_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
