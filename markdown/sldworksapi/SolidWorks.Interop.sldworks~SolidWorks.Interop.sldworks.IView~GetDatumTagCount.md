---
title: "GetDatumTagCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDatumTagCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTagCount.html"
---

# GetDatumTagCount Method (IView)

Gets the number of datum tags on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumTagCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetDatumTagCount()
```

### C#

```csharp
System.int GetDatumTagCount()
```

### C++/CLI

```cpp
System.int GetDatumTagCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of datum tags

## VBA Syntax

See [View::GetDatumTagCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetDatumTagCount.html).

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetDatumTags](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDatumTags.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumTags Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTags.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
