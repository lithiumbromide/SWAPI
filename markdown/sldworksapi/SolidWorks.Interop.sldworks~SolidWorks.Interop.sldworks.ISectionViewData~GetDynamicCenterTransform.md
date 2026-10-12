---
title: "GetDynamicCenterTransform Method (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "GetDynamicCenterTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetDynamicCenterTransform.html"
---

# GetDynamicCenterTransform Method (ISectionViewData)

Gets the translation between the center of the model and the plane in the specified section in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDynamicCenterTransform( _
   ByVal Index As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim Index As System.Integer
Dim value As MathTransform

value = instance.GetDynamicCenterTransform(Index)
```

### C#

```csharp
MathTransform GetDynamicCenterTransform(
   System.int Index
)
```

### C++/CLI

```cpp
MathTransform^ GetDynamicCenterTransform(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Section (see **Remarks**)

### Return Value

[Translation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html) between the center of the model and the plane in the section specified for Index

## VBA Syntax

See [SectionViewData::GetDynamicCenterTransform](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~GetDynamicCenterTransform.html).

## Examples

[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

## Remarks

This method is only valid for section views having more than one section. Specify:

- 1 for Section 1
- 2 for Section 2
- 3 for Section 3

If the section view contains only one section and you specify 1 for Index, then this method returns Nothing or null.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2015 SP2, Revision Number 23.2
