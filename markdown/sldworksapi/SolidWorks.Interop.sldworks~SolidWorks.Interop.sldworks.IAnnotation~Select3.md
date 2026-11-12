---
title: "Select3 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "Select3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select3.html"
---

# Select3 Method (IAnnotation)

Selects this annotation and marks it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select3( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select3(Append, Data)
```

### C#

```csharp
System.bool Select3(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select3(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends this selection to the current selection list, false replaces the current selection list with this selection
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the annotation was selected, false if not

## VBA Syntax

See [Annotation::Select3](ms-its:sldworksapivb6.chm::/sldworks~Annotation~Select3.html).

## Examples

[Get Corresponding Note in Assembly (VBA)](Get_Corresponding_Note_in_Assembly_Example_VB.htm)
[Get Corresponding Note in Part (VBA)](Get_Corresponding_Note_in_Part_Example_VB.htm)
[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)
[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
