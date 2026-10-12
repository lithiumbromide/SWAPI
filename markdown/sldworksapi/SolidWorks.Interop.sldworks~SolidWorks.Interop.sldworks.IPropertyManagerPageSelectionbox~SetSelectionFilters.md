---
title: "SetSelectionFilters Method (IPropertyManagerPageSelectionbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageSelectionbox"
member: "SetSelectionFilters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetSelectionFilters.html"
---

# SetSelectionFilters Method (IPropertyManagerPageSelectionbox)

Defines the types of objects the user can select for this selection box.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSelectionFilters( _
   ByVal Filters As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageSelectionbox
Dim Filters As System.Object

instance.SetSelectionFilters(Filters)
```

### C#

```csharp
void SetSelectionFilters(
   System.object Filters
)
```

### C++/CLI

```cpp
void SetSelectionFilters(
   System.Object^ Filters
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Filters`: Array of filter values as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (see **Remarks**)

## VBA Syntax

See [PropertyManagerPageSelectionbox::SetSelectionFilters](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageSelectionbox~SetSelectionFilters.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

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
[IPropertyManagerPageSelectionbox::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ISetSelectionFilters.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
