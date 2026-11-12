---
title: "GetAnnotation Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetAnnotation.html"
---

# GetAnnotation Method (ITableAnnotation)

Gets the annotation for this table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
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

[IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object

## VBA Syntax

See [TableAnnotation::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetAnnotation.html).

## Examples

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)
[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)
[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
