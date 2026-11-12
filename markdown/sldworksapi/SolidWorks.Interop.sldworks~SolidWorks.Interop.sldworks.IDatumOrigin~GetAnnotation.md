---
title: "GetAnnotation Method (IDatumOrigin)"
project: "SOLIDWORKS API Help"
interface: "IDatumOrigin"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetAnnotation.html"
---

# GetAnnotation Method (IDatumOrigin)

Gets the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object for this datum origin.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumOrigin
Dim value As Annotation

value = instance.GetAnnotation()
```

### C#

```csharp
Annotation GetAnnotation()
```

### C++/CLI

```cpp
Annotation^ GetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object for this annotation

## VBA Syntax

See [DatumOrigin::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~DatumOrigin~GetAnnotation.html).

## Examples

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

## Remarks

The IAnnotation object is a higher-level object that contains methods that apply to all types of annotations.

## See Also

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.html)
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
