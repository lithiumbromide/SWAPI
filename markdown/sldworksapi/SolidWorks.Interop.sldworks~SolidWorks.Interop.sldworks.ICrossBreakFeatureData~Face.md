---
title: "Face Property (ICrossBreakFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICrossBreakFeatureData"
member: "Face"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData~Face.html"
---

# Face Property (ICrossBreakFeatureData)

Gets or sets the face to which to apply this cross break feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Face As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICrossBreakFeatureData
Dim value As System.Object

instance.Face = value

value = instance.Face
```

### C#

```csharp
System.object Face {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Face {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) to which to apply this cross break feature

## VBA Syntax

See [CrossBreakFeatureData::Face](ms-its:sldworksapivb6.chm::/sldworks~CrossBreakFeatureData~Face.html).

## Examples

[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

## See Also

[ICrossBreakFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.html)
[ICrossBreakFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
