---
title: "GetAnnotation Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetAnnotation.html"
---

# GetAnnotation Method (IDatumTag)

Gets the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object for this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Object

value = instance.GetAnnotation()
```

### C#

```csharp
System.object GetAnnotation()
```

### C++/CLI

```cpp
System.Object^ GetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Annotation

## VBA Syntax

See [DatumTag::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetAnnotation.html).

## Examples

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

## Remarks

The [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object is a higher-level object that contains methods that apply to all types of annotations.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetAnnotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
