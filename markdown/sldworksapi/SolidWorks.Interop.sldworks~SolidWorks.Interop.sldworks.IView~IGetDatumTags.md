---
title: "IGetDatumTags Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDatumTags"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTags.html"
---

# IGetDatumTags Method (IView)

Gets all the datum tags on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDatumTags( _
   ByVal NumDatumTag As System.Integer _
) As DatumTag
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumDatumTag As System.Integer
Dim value As DatumTag

value = instance.IGetDatumTags(NumDatumTag)
```

### C#

```csharp
DatumTag IGetDatumTags(
   System.int NumDatumTag
)
```

### C++/CLI

```cpp
DatumTag^ IGetDatumTags(
   System.int NumDatumTag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDatumTag`: Total number of datum tags on the drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [datum tags](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of datum tags all at once instead of calling [IView::GetFirstDatumTag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDatumTag.html) and then repeatedly calling [IDatumTag::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~GetNext.html) to obtain the remaining datum tags on this drawing view.

Before calling this method, call [IView::GetDatumTagCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDatumTagCount.html) to get the value for numDatumTag.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumTagCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTagCount.html)
[IView::GetDatumTags Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTags.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
