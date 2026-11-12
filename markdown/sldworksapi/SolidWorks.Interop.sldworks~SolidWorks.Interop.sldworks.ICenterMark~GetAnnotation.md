---
title: "GetAnnotation Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetAnnotation.html"
---

# GetAnnotation Method (ICenterMark)

Gets the annotation for this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
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

[Annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object

## VBA Syntax

See [CenterMark::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~GetAnnotation.html).

## Examples

[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)
[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

## Remarks

This method returns null or nothing for center marks created as features (earlier style of center marks). See [ICenterMark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html) for details about the old and new style center marks. See SOLIDWORKS Help for details about center marks.

For example, if [ISelectionMgr::GetSelectedObjectType3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html) equals swSelCENTERMARKS, then ICenterMark::GetAnnotation equals null or nothing. But, if ISelectionMgr::GetSelectedObjectType3 equals swSelCENTERMARKSYMS, then ICenterMark::GetAnnotation points to the IAnnotation object.

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
