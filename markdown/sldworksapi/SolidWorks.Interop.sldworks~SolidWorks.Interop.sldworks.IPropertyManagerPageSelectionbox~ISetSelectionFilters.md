---
title: "ISetSelectionFilters Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "ISetSelectionFilters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ISetSelectionFilters.html"
---

# ISetSelectionFilters Method (IPropertyManagerPageSelectionbox)

Defines the types of objects the user can select for this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetSelectionFilters( _
   ByVal FilterCount As System.Short, _
   ByRef Filters As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim FilterCount As System.Short
Dim Filters As System.Integer

instance.ISetSelectionFilters(FilterCount, Filters)
```

### C#

```csharp
void ISetSelectionFilters(
   System.short FilterCount,
   ref System.int Filters
)
```

### C++/CLI

```cpp
void ISetSelectionFilters(
   System.short FilterCount,
   System.int% Filters
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilterCount`: Number of filters
- `Filters`: - in-procses, unmanaged C++: Array of filter values as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

When a user makes a selection in the graphics area, SOLIDWORKS must decide whether to select a face, body, or component. The following table shows what appears in a selection box created with the specifed filters after a selection occurs in the graphics area.

| Filters | Result |
| --- | --- |
| swSelFACES, swSelSOLIDBODIES | Face If you want a body to appear in the selection box, then use swSelSOLIDBODIESFIRST. |
| swSelFACES, swSelCOMPONENTS | Component If you want a face to appear in the selection box, then use swSELCOMPSDONTOVERRIDE. |
| swSelSOLIDBODIES, swSelCOMPONENTS | Component If you want a body to appear in the selection box, then use swSelSOLIDBODIESFIRST. |
| swSelFACES, swSelSOLIDBODIES, swSelCOMPONENTS | Component If you want a face to appear in the selection box, then use swSelCOMPSDONTOVERRIDE. - or - If you want a body to appear in the selection box, then use swSelSOLIDBODIESFIRST. |

swSelSURFACEBODIES and swSelSURFBODIESFIRST behave simliar to swSelSOLIDBODIES and swSelSOLIDBODIESFIRST. swSelEDGES and swSelVERTICES behave similar to swSelFACES. If the Filters is set to swSelNOTHING or swSelUNSUPPORTED, this the call to this method fails.

## See Also

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.html)
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
