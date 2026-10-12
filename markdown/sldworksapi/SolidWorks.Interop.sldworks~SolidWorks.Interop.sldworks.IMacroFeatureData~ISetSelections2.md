---
title: "ISetSelections2 Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "ISetSelections2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetSelections2.html"
---

# ISetSelections2 Method (IMacroFeatureData)

Sets the selected objects for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSelections2( _
   ByVal SelCount As System.Integer, _
   ByRef Objects As System.Object, _
   ByRef SelMarks As System.Integer, _
   ByRef DrViews As View _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim SelCount As System.Integer
Dim Objects As System.Object
Dim SelMarks As System.Integer
Dim DrViews As View

instance.ISetSelections2(SelCount, Objects, SelMarks, DrViews)
```

### C#

```csharp
void ISetSelections2(
   System.int SelCount,
   ref System.object Objects,
   ref System.int SelMarks,
   ref View DrViews
)
```

### C++/CLI

```cpp
void ISetSelections2(
   System.int SelCount,
   System.Object^% Objects,
   System.int% SelMarks,
   View^% DrViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelCount`: Number of selected objects
- `Objects`: - in-process, unmanaged C++: Pointer to an array of objects as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) of size SelCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `SelMarks`: - in-process, unmanaged C++: Pointer to an array of marks (integers or longs) of size SelCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `DrViews`: - in-process, unmanaged C++: Pointer to an array of [drawing views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) of size selCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The method expects to be passed three arrays of the same size.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelections3.html)
[IMacroFeatureData::IGetSelections3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetSelections3.html)
[IMacroFeatureData::SetSelections2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetSelections2.html)
[IMacroFeatureData::GetSelectionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetSelectionCount.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
