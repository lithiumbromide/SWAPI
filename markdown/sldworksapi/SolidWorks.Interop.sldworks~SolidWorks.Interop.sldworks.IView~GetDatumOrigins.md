---
title: "GetDatumOrigins Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDatumOrigins"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins.html"
---

# GetDatumOrigins Method (IView)

Gets all of the datum origins on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumOrigins() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDatumOrigins()
```

### C#

```csharp
System.object GetDatumOrigins()
```

### C++/CLI

```cpp
System.Object^ GetDatumOrigins();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [datum origins](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin.html)

## VBA Syntax

See [View::GetDatumOrigins](ms-its:sldworksapivb6.chm::/sldworks~View~GetDatumOrigins.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

Use this method to obtain the array of datum origins all at once instead of calling [IView::GetFirstDatumOrigin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDatumOrigin.html) and then repeatedly calling [IDatumOrigin::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin~GetNext.html) to obtain the remaining datum origins on this drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumOriginCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOriginCount.html)
[IView::IGetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumOrigins.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
