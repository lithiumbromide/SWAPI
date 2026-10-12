---
title: "GetAnnotation Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAnnotation.html"
---

# GetAnnotation Method (INote)

Gets the annotation for this specific note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
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

[Annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [Note::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~Note~GetAnnotation.html).

## Examples

[Get All Notes in Drawing Template (VBA)](Get_All_Notes_in_Drawing_Template_Example_VB.htm)
[Insert Note (VBA)](Insert_a_Note_Example_VB.htm)
[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)
[Set BOM Balloon Text (VBA)](Set_BOM_Balloon_Example_VB.htm)
[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

## Remarks

This method obtains the owning [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object for this [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) object. The IAnnotation object is a higher-level object that contains methods that are general to all types of annotations.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAnnotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
