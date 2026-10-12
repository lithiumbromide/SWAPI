---
title: "GetFaceCount Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFaceCount.html"
---

# GetFaceCount Method (IMidSurface3)

Gets the number of faces in the midsurface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim value As System.Integer

value = instance.GetFaceCount()
```

### C#

```csharp
System.int GetFaceCount()
```

### C++/CLI

```cpp
System.int GetFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces in this midsurface feature, including a null face (separator) between the front and back face, which counts as one face

## VBA Syntax

See [MidSurface3::GetFaceCount](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetFaceCount.html).

## Examples

[Insert MidSurface in Component (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)

## Remarks

If more than one reference surface exists in the midsurface feature, then those faces are included in the total.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFace.html)
[IMidSurface3::GetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFaceArray.html)
[IMidSurface3::GetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFace.html)
[IMidSurface3::GetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFaceArray.html)
[IMidSurface3::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFace.html)
[IMidSurface3::IGetFirstFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstFaceArray.html)
[IMidSurface3::IGetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFace.html)
[IMidSurface3::IGetNextFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFaceArray.html)
[IMidSurface3::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFaces.html)
[IMidSurface3::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFaces.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
