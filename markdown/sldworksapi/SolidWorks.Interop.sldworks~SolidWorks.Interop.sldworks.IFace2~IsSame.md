---
title: "IsSame Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IsSame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IsSame.html"
---

# IsSame Method (IFace2)

Gets whether the two faces are the same.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSame( _
   ByVal FaceIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim FaceIn As System.Object
Dim value As System.Boolean

value = instance.IsSame(FaceIn)
```

### C#

```csharp
System.bool IsSame(
   System.object FaceIn
)
```

### C++/CLI

```cpp
System.bool IsSame(
   System.Object^ FaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceIn`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to which to compare this face

### Return Value

True if the two faces are the same, false if they are different

## VBA Syntax

See [Face2::IsSame](ms-its:sldworksapivb6.chm::/sldworks~Face2~IsSame.html).

## Examples

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IIsSame Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IIsSame.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
