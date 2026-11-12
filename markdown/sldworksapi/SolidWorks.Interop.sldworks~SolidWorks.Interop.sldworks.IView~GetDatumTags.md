---
title: "GetDatumTags Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDatumTags"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTags.html"
---

# GetDatumTags Method (IView)

Gets all of the datum tags on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumTags() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDatumTags()
```

### C#

```csharp
System.object GetDatumTags()
```

### C++/CLI

```cpp
System.Object^ GetDatumTags();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [datum tags](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag.html)

## VBA Syntax

See [View::GetDatumTags](ms-its:sldworksapivb6.chm::/sldworks~View~GetDatumTags.html).

## Examples

[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Use this method to obtain the array of datum tags all at once instead of calling [IView::GetFirstDatumTag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDatumTag.html) and then repeatedly calling [IDatumTag::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~GetNext.html) to obtain the remaining datum tags on this drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumTagCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTagCount.html)
[IView::IGetDatumTags Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTags.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
