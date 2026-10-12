---
title: "GetFaceCount Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaceCount.html"
---

# GetFaceCount Method (ISimpleFilletFeatureData2)

Gets the number of faces on which to create a simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceCount( _
   ByVal WhichFaceList As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim WhichFaceList As System.Integer
Dim value As System.Integer

value = instance.GetFaceCount(WhichFaceList)
```

### C#

```csharp
System.int GetFaceCount(
   System.int WhichFaceList
)
```

### C++/CLI

```cpp
System.int GetFaceCount(
   System.int WhichFaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichFaceList`: Face as defined in [swSimpleFilletWhichFaces_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletWhichFaces_e.html)

### Return Value

Number of faces

## VBA Syntax

See [SimpleFilletFeatureData2::GetFaceCount](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetFaceCount.html).

## Examples

[Get Data for Simple Fillet (C#)](Get_Data_for_Simple_Fillet_Example_CSharp.htm)
[Get Data for Simple Fillet (VB.NET)](Get_Data_for_Simple_Fillet_Example_VBNET.htm)
[Get Data for Simple Fillet (VBA)](Get_Data_for_Simple_Fillet_Example_VB.htm)

## Remarks

Call this method before calling [ISimpleFilletFeatureData2::IGetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetFaces.html) to get the size of the array for that method.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFaces.html)
[ISimpleFilletFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFaces.html)
[ISimpleFilletFeatureData2::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~SetFaces.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
